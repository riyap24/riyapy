import hashlib
import os

def file_hash(filename):
    sha = hashlib.sha256()
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()

# 1. Get the exact folder where this Python script lives
script_directory = os.path.dirname(os.path.abspath(__file__))

# 2. Set the target file to be inside that exact same folder
filename = os.path.join(script_directory, "sample.txt")

# 3. If the file doesn't exist, automatically create it with some text
if not os.path.exists(filename):
    print(f"Creating a new test file at: {filename}")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Hello, this is a test file for calculating the hash value!")

# 4. Calculate and print the hash
print("Calculating hash...")
print("File Hash:", file_hash(filename))
