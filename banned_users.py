banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a respinse if you wish.")

car = 'subaru'
print("is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car 'audi'? I predict False.")
print(car == 'audi')

name = 'eduardo'
other_name = 'Eduardo'
# other_name.lower() it only temporarily lowers case.
print(name == other_name.lower())
num_1 = 20
num_2 = 22
num_3 = 21

print(num_1 <= num_2 or num_3 >= num_1)

items = ['juice', 'milk', 'apple', 'guava']
# if 'mango' in items:
#     print(f"We have it!")
# else:
#     print("We're out!")
if 'juice' in items:
    print("Got it!")
else:
    print("Naaa")