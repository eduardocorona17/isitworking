# prompt = "\nTell me something to repeat: "
# prompt += "\nEnter quit to end program: "
# message = ""
# while message != "quit":
#     message = input(prompt)
#     print(message)

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("What country would you like to visit? ")

    responses[name] = response

    repeat = input("Would you like another friend to respond? (y/n) ")
    if repeat == 'n':
        polling_active = False
    
print("\n---Results---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}")
