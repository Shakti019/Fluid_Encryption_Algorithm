import os
import time
import memory_profiler
import matplotlib.pyplot as plt
import pandas as pd
from Fluid import convert_pwd_in_array


def load_txt_file(file_name):
    try:
        txt_file_path = os.path.join(os.getcwd(), file_name)
        with open(txt_file_path, "r", encoding="utf-8", errors="ignore") as file:
            passwords = file.readlines()
        passwords = [password.strip() for password in passwords]
        if not passwords:
            raise ValueError("The TXT file is empty or contains no passwords.")

        print(f"Loaded TXT file '{file_name}' successfully.")
        return pd.DataFrame({"password": passwords})
    except Exception as e:
        print(f"Error loading TXT file: {e}")
        return pd.DataFrame()


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
        print("Memory Usages:", encryption_memory)
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

    return results


def plot_individual_graphs(df):
    plt.style.use('ggplot')

    # Encryption Time
    plt.figure(figsize=(10, 6))
    plt.plot(df["Password"], df["Encryption Time (s)"], label="Encryption Time (s)", color="dodgerblue",
             marker="o", linewidth=2)
    plt.title("Encryption Time for Each Password")
    plt.xlabel("Password")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Encryption Memory Usage
    plt.figure(figsize=(10, 6))
    plt.plot(df["Password"], df["Encryption Memory (MB)"], label="Encryption Memory (MB)", color="salmon",
             marker="x", linewidth=2)
    plt.title("Encryption Memory Usage for Each Password")
    plt.xlabel("Password")
    plt.ylabel("Memory (MB)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Throughput
    plt.figure(figsize=(10, 6))
    plt.plot(df["Password"], df["Throughput (chars/s)"], label="Throughput (chars/s)", color="mediumseagreen",
             marker="s", linewidth=2)
    plt.title("Encryption Throughput for Each Password")
    plt.xlabel("Password")
    plt.ylabel("Throughput (chars/s)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Decryption Memory Usage
    plt.figure(figsize=(10, 6))
    plt.plot(df["Password"], df["Decryption Memory (MB)"], label="Decryption Memory (MB)", color="orange",
             marker="d", linewidth=2)
    plt.title("Decryption Memory Usage for Each Password")
    plt.xlabel("Password")
    plt.ylabel("Memory (MB)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Decryption Accuracy
    plt.figure(figsize=(10, 6))
    plt.plot(df["Password"], df["Decryption Accuracy (%)"], label="Decryption Accuracy (%)", color="purple",
             marker="v", linewidth=2)
    plt.title("Decryption Accuracy for Each Password")
    plt.xlabel("Password")
    plt.ylabel("Accuracy (%)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Password Length vs. Throughput
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Password Length"], df["Throughput (chars/s)"], label="Password Length vs Throughput", color="teal",
                s=70)
    plt.title("Password Length vs. Throughput")
    plt.xlabel("Password Length")
    plt.ylabel("Throughput (chars/s)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    txt_file_name = "data1.txt"
    df = load_txt_file(txt_file_name)
    if not df.empty:
        results = test_encryption_decryption(df)
        result_df = pd.DataFrame(results)
        plot_individual_graphs(result_df)


    print("Processing complete. Exiting program.")
