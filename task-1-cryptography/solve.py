import base64

encoded_text = "QkFJTntiQTczX1E4Ul9BcmhIQ19YNHlHY0R9"

# Step 1: Base64 decoding
decoded_text = base64.b64decode(encoded_text).decode()

print("After Base64 decoding:")
print(decoded_text)

# Step 2: Vigenere decryption
ciphertext = decoded_text
key = "ACPJ"

result = ""
key_index = 0

for char in ciphertext:
    if char.isalpha():

        shift = ord(key[key_index % len(key)]) - ord('A')

        if char.isupper():
            result += chr(
                (ord(char) - ord('A') - shift) % 26 + ord('A')
            )

        else:
            result += chr(
                (ord(char) - ord('a') - shift) % 26 + ord('a')
            )

        key_index += 1

    else:
        result += char

print("\nDecrypted result:")
print(result)
