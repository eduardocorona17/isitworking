current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1


prompt = input("What shall I repeat to you ('q' to quit)? ")
# prompt += "\nEnter 'Quit' when you are finished. "
active = True
while active:  
    message = input(prompt)
    if message == 'q':
        active = False
    else:    
        print(message)