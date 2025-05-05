import time
import tracemalloc
import matplotlib.pyplot as plt
import random
import string
from Fluid import convert_pwd_in_array
from Fluid import reverse_fluid_encrypt
from Fluid import get_system_hardware_info


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def test_encryption_decryption(password):
    start_time = time.time()
    tracemalloc.start()
    binary_list = convert_pwd_in_array(password)
    encryption_time = time.time() - start_time
    encryption_memory = tracemalloc.get_traced_memory()[1]  # Peak memory usage
    tracemalloc.stop()


    xor_results, original_bit = binary_list[:2]
    mac_address, system_info = get_system_hardware_info()
    # Decrypt and check for accuracy
    start_time = time.time()
    tracemalloc.start()  # Start tracking memory
    decrypted_bits, decrypted_password = reverse_fluid_encrypt(xor_results, original_bit, mac_address, system_info)
    decryption_time = time.time() - start_time
    decryption_memory = tracemalloc.get_traced_memory()[1]  # Peak memory usage
    tracemalloc.stop()

    # Check accuracy
    accuracy = decrypted_password == password

    return {
        "encryption_time": encryption_time,
        "decryption_time": decryption_time,
        "encryption_memory": encryption_memory,
        "decryption_memory": decryption_memory,
        "accuracy": accuracy
    }

def run_tests(num_tests=1):
    lengths = [5, 10]
    results = []

    for length in lengths:
        length_results = []
        for _ in range(num_tests):
            password = generate_random_password(length)
            result = test_encryption_decryption(password)
            length_results.append(result)

        avg_encryption_time = sum(r['encryption_time'] for r in length_results) / num_tests
        avg_decryption_time = sum(r['decryption_time'] for r in length_results) / num_tests
        avg_encryption_memory = sum(r['encryption_memory'] for r in length_results) / num_tests
        avg_decryption_memory = sum(r['decryption_memory'] for r in length_results) / num_tests
        accuracy = sum(1 for r in length_results if r['accuracy']) / num_tests
        throughput = num_tests / (avg_encryption_time + avg_decryption_time)

        results.append({
            "length": length,
            "avg_encryption_time": avg_encryption_time,
            "avg_decryption_time": avg_decryption_time,
            "avg_encryption_memory": avg_encryption_memory,
            "avg_decryption_memory": avg_decryption_memory,
            "accuracy": accuracy,
            "throughput": throughput
        })

    return results

def plot_results(results):
    """Plot the results of the test."""
    lengths = [r['length'] for r in results]
    encryption_times = [r['avg_encryption_time'] for r in results]
    decryption_times = [r['avg_decryption_time'] for r in results]
    encryption_memories = [r['avg_encryption_memory'] for r in results]
    decryption_memories = [r['avg_decryption_memory'] for r in results]
    accuracies = [r['accuracy'] * 100 for r in results]  # Percentage
    throughputs = [r['throughput'] for r in results]

    # Plot encryption and decryption times
    plt.figure(figsize=(12, 6))
    plt.plot(lengths, encryption_times, label='Encryption Time (s)', marker='o')
    plt.plot(lengths, decryption_times, label='Decryption Time (s)', marker='o')
    plt.xlabel('Password Length')
    plt.ylabel('Time (s)')
    plt.title('Encryption and Decryption Time by Password Length')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot encryption and decryption memory usage
    plt.figure(figsize=(12, 6))
    plt.plot(lengths, encryption_memories, label='Encryption Memory (bytes)', marker='o')
    plt.plot(lengths, decryption_memories, label='Decryption Memory (bytes)', marker='o')
    plt.xlabel('Password Length')
    plt.ylabel('Memory Usage (bytes)')
    plt.title('Encryption and Decryption Memory Usage by Password Length')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot accuracy
    plt.figure(figsize=(12, 6))
    plt.plot(lengths, accuracies, label='Accuracy (%)', marker='o')
    plt.xlabel('Password Length')
    plt.ylabel('Accuracy (%)')
    plt.title('Decryption Accuracy by Password Length')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot throughput
    plt.figure(figsize=(12, 6))
    plt.plot(lengths, throughputs, label='Throughput (passwords/s)', marker='o')
    plt.xlabel('Password Length')
    plt.ylabel('Throughput (passwords/s)')
    plt.title('Throughput by Password Length')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    results = run_tests()
    plot_results(results)
