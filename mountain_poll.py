responses = {}
polling_active = True
while polling_active:

    name = input("\nWhat is your name? ")
    response = input("What cool mountains have you climbed? ")
    responses[name] = response

    repeat = input("Let another respond (y/n)? ")
    if repeat == 'n':
        polling_active = False
    # print(f"{name} has climbed {response}!")
print("The total correspondants have polled and this is the outcome:")
for name, response in responses.items():
    print(f"{name} has climbed {response}!")
