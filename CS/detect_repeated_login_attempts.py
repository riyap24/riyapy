login_attempts = {
    "user1": 2,
    "user2": 7,
    "user3": 4,
    "user4": 10
}

limit = 5

for user, attempts in login_attempts.items():
    if attempts >= limit:
        print(user, "Suspicious login activity")
    else:
        print(user, "Normal activity")