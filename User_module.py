class Users:
    def __init__(self, first_name, last_name, location, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print(f"The following info is collected from the user:\n{self.first_name} {self.last_name}\n{self.location}\n{self.age}\n{self.username}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.username} logged in {self.login_attempts} times.")
    
    def reset_logins(self):
        self.login_attempts = 0
        print(f"Attempts to log in have been reset to {self.login_attempts}")

