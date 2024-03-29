import json

def get_stored_username():
    """Retrieve username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username()
        print(f"We'll rememer you when you come back, {username}!")
greet_user()