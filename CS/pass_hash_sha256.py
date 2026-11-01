import hashlib

password = input("Enter password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

print("Original Password:", password)
print("Hashed Password:", hashed)