def divide(a, b):
    return a / b

password = "admin123"

def get_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user

print("done")
