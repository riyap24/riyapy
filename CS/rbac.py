users = {
    "admin": ["read", "write", "delete"],
    "teacher": ["read", "write"],
    "student": ["read"]
}

username = input("Enter username: ")
action = input("Enter action: ")

if username in users:
    if action in users[username]:
        print("Access Granted")
    else:
        print("Access Denied")
else:
    print("User Not Found")