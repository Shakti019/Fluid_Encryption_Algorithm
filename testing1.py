import os
import time
import memory_profiler
import matplotlib.pyplot as plt
import pandas as pd
import sys
from Fluid import convert_pwd_in_array
from pympler import asizeof


def load_sample_data():
    passwords = ["password123", "securePass!", "helloWorld2024", "Test@456", "OpenAIrocks!"]
    return pd.DataFrame({"password": passwords})


def test_encryption_decryption(df):
    results = []
    for idx, row in df.iterrows():
        print("Tested Data", idx)
        password = row["password"]
        password_len = len(password)
        print(f"Password length: {password_len}")

        start_time = time.time()
        start_mem = memory_profiler.memory_usage()[0]
        decrypted_string = convert_pwd_in_array(password)
        end_mem = memory_profiler.memory_usage()[0]
        encryption_time = time.time() - start_time
        print("Encryption time:", encryption_time)
        encryption_memory = end_mem - start_mem
        print("Memory Usage:", encryption_memory)
        throughput = password_len / encryption_time if encryption_time > 0 else 0
        print("Throughput:", throughput)

        decryption_memory = memory_profiler.memory_usage()[0] - end_mem
        accuracy = (decrypted_string == password) * 100
        print("Accuracy:", accuracy)

        results.append({
            "Password": idx + 1,
            "Password Length": password_len,
            "Encryption Time (s)": encryption_time,
            "Encryption Memory (MB)": encryption_memory,
            "Throughput (chars/s)": throughput,
            "Decryption Memory (MB)": decryption_memory,
            "Decryption Accuracy (%)": accuracy,
        })

        # Print memory size of results after each iteration
        results_size = sys.getsizeof(results)  # Size without references
        full_results_size = asizeof.asizeof(results)  # Size including all references
        print(f"Current results list size (shallow): {results_size} bytes")
        print(f"Current results list size (deep): {full_results_size} bytes")

    return results


def plot_results(df):
    plt.style.use('ggplot')


    parameters = {
        "Encryption Time (s)": "Encryption Time (s)",
        "Encryption Memory (MB)": "Encryption Memory Usage (MB)",
        "Throughput (chars/s)": "Throughput (chars/s)",
        "Decryption Memory (MB)": "Decryption Memory Usage (MB)",
        "Decryption Accuracy (%)": "Decryption Accuracy (%)",
        "Password Length": "Password Length",
    }

    for column, title in parameters.items():
        plt.figure(figsize=(10, 6))
        plt.plot(df["Password"], df[column], label=title, marker="o")
        plt.title(title)
        plt.xlabel("Password Index")
        plt.ylabel(title)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    df = load_sample_data()
    results = test_encryption_decryption(df)
    result_df = pd.DataFrame(results)
    plot_results(result_df)

    print("Processing complete. Exiting program.")
