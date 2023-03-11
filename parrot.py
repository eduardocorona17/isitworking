prompt = "\nTell me something to repeat to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True

message = ""
while active:
# while message != 'quit':
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)