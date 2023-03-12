def greet_users(users):
    for user in users:
        print(f"Hello, {user.title()}!")

usies = ['eddie', 'chuy', 'james', 'mikey']

greet_users(usies)