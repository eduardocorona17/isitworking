dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
# for dimen in dimensions:
#     print(dimen)
print("Our original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

buffet = ('Pizza', 'Pasta', 'Sandwhiches', 'Beer', 'Liquor')
print("Here are the items we offer: ")
for food in buffet:
    print(f"{food}")
buffet = ("Pizza", "Pasta", "Sandwhiches", "Apple Juice", "Milk")
print("We lost our liquor license: ")
for food in buffet:
    print(f"{food}")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)
new_users = []
# current_users = ['Eduardocorona', 'aliceabc', 'LILY', 'Clarence']
# user_name = input("Please enter a new user name (enter 'q' to finish): ")
# while user_name != 'q':
# if user_name in current_users:
#     print(f"Error! {user_name} is already used")
#     print(f"Please enter a {user_name}")
# else:
#     new_users.append(user_name)
# print(new_users)
# print()
# for user in current_users:
#     user.lower()
#     if user_name in current_users:
#         print(f"Sorry {user_name} is already taken try again: ")
#         print(f"Enter {user_name}")
#     else:
#         new_users.append(user_name)
# print(current_users)
        
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Yee")
else: print("Nee")
if 'pepperoni' in requested_toppings:
    print("Yee")
else: print("Nee")