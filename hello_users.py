usernames = ['eduarthough', 'edgarfaeday', 'juni', 'lizbeth', 'lori']
new_users = ['jay', 'rudolph', 'JUNI', 'james', 'eddie']

for new_user in new_users:
    if new_user in usernames:
        print(f"Sorry, {new_user.title()} is taken.")
    else:
        print(f"Welcome to the mobile app, {new_user.title()}!")

usernames2 = usernames[:]

for user in new_users:
    if user.lower() in usernames:
        print(f"{user} is taken, choose a different username.")
    else:
        print(f"Welcome aboard, {user}!")

original_nums = list(range(1,10))

for num in original_nums:
    
    if num == 1 in original_nums:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else: print(f"{num}th")

# for num in original_nums[3:10]:
#     print(f"{num}th")
# for num in original_nums[2:3]:
#      print(f"{num}rd")
# for num in original_nums[1:2]:
#     print(f"{num}nd")
# for num in original_nums[:1]:
#     print(f"{num}st")
