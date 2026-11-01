text = input("Enter encrypted message: ")
shift = 3

decrypted = ""

for char in text:
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')

        decrypted += chr(
            (ord(char) - base - shift) % 26 + base
        )
    else:
        decrypted += char

print("Decrypted Message:", decrypted)