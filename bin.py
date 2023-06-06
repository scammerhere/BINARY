def text_to_binary(text):
    binary_string = ""
    for char in text:
        # Convert each character to its ASCII value
        ascii_value = ord(char)
        # Convert the ASCII value to binary representation
        binary_value = bin(ascii_value)[2:]  # [2:] removes the "0b" prefix
        # Pad the binary value with leading zeros to make it 8 bits long
        padded_binary = binary_value.zfill(8)
        # Append the padded binary value to the final binary string
        binary_string += padded_binary
    return binary_string

# Example usage
input_text = input("Enter the text to encrypt: ")
encrypted_binary = text_to_binary(input_text)
print("Encrypted binary: ", encrypted_binary)
