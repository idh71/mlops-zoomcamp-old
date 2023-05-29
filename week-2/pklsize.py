import os

file_path = "./output/dv.pkl"

# Get the file size in bytes
file_size = os.path.getsize(file_path)

# Convert bytes to a human-readable format
size_in_kb = file_size / 1024
size_in_mb = size_in_kb / 1024
size_in_gb = size_in_mb / 1024

print(f"File Size: {file_size} bytes")
print(f"File Size: {size_in_kb:.2f} KB")
print(f"File Size: {size_in_mb:.2f} MB")
print(f"File Size: {size_in_gb:.2f} GB")