filename = 'files_exceptions/guest.txt'

prompt = input("what is your name? ")
name = input(prompt)

with open(filename, 'w') as file_object:
    file_object.write("Eduardo")
