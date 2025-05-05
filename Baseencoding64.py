import base64

# Base64 string with padding
encoded_string = "A9743tOXDAKusxtj4pG/nNKUWUSCO"

# Add padding to make the length a multiple of 4
encoded_string_padded = encoded_string + '=' * ((4 - len(encoded_string) % 4) % 4)

# Decode the Base64 string into bytes
decoded_bytes = base64.b64decode(encoded_string_padded)

# Convert the decoded bytes into binary
binary_representation = ''.join(format(byte, '08b') for byte in decoded_bytes)
binary_representation
