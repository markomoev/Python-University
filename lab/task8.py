binary_file = open("binary_file.bin", "wb+")
text = "Hello123"
encoded = text.encode()
binary_file.write(encoded)
binary_file.seek(0)
binary_data = binary_file.read()
print(binary_data)
decoded = binary_data.decode()
print(decoded)