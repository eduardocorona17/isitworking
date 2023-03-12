responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is thy name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")