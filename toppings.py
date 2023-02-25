requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we are out of {requested_topping}.")
    else:
        print(f"Adding {requested_topping.title()}.")

print("\nAll done!")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings2 = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings2:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}.")
    else:
        print(f"Sorry, we do not have {requested_topping.title()}.")
print(f"\nAll finished with your pizza!")
# if 'mushrooms' in requested_toppings:
#     print("Adding mushies.")
# if 'pepperoni' in requested_toppings:
#     print("Adding p-p-roni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra queso.")
# print("Donzo with your pizza.")