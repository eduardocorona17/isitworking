# import json

# def get_num():
#     filename = 'favorite_num.txt'
#     try:
#         number = int(input("What is your favorite number? "))
#         with open(filename, 'w') as f:
#             json.dump(number, f)
#     except FileNotFoundError:
#         pass


# def retieve_num():
#     filename = 'favorite_num.txt'
#     try:
#         with open(filename) as f:
#             filename = json.load(f)
#             print(f"Your favorite number is {filename}.")
#     except FileNotFoundError:
#         # print(f"Sorry, {filename} does not exist!")
#         get_num()


