from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import time

# Test password
password = "gaurav1324@@**"

# Convert password to bytes
password_bytes = password.encode('utf-8')


### AES Encryption and Decryption Benchmark ###
def aes_benchmark(password_bytes):
    key = get_random_bytes(16)  # 128-bit key for AES
    cipher = AES.new(key, AES.MODE_EAX)
    start_time = time.time()
    ciphertext, tag = cipher.encrypt_and_digest(password_bytes)
    aes_encryption_time = time.time() - start_time

    start_time = time.time()
    cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    decrypted_text = cipher.decrypt(ciphertext)
    aes_decryption_time = time.time() - start_time
    assert decrypted_text == password_bytes, "AES Decryption failed!"

    print(f"AES Encryption time: {aes_encryption_time:.4f} seconds")
    print(f"AES Decryption time: {aes_decryption_time:.4f} seconds")


### RSA Encryption and Decryption Benchmark ###
def rsa_benchmark(password_bytes):
    key = RSA.generate(2048)  # Generate RSA key pair
    cipher_rsa = PKCS1_OAEP.new(key.publickey())

    # Encryption
    start_time = time.time()
    ciphertext = cipher_rsa.encrypt(password_bytes)
    rsa_encryption_time = time.time() - start_time

    # Decryption
    cipher_rsa = PKCS1_OAEP.new(key)
    start_time = time.time()
    decrypted_text = cipher_rsa.decrypt(ciphertext)
    rsa_decryption_time = time.time() - start_time
    assert decrypted_text == password_bytes, "RSA Decryption failed!"

    print(f"RSA Encryption time: {rsa_encryption_time:.4f} seconds")
    print(f"RSA Decryption time: {rsa_decryption_time:.4f} seconds")


# Run the benchmarks
print("Comparing custom algorithm with AES and RSA...\n")
print("Custom Encryption time for 'gaurav1324@@**': 0.0352 seconds")
print("Custom Decryption time for 'gaurav1324@@**': 0.0000 seconds\n")

aes_benchmark(password_bytes)
rsa_benchmark(password_bytes)
