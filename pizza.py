# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
# for topping in pizza['toppings']:
#     print(f"\t+ {topping}")

def make_pizza(*toppings):
    """Summarize pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')