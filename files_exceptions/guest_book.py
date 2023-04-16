filename = 'files_exceptions/guest_book.txt'
while True:
    name = input("What is your name? enter 'quit' to stop. ")
    if name.lower() == 'quit':
        break
    else:
        print(f"Hello, {name}!")
        with open(filename, 'a') as object_file:
            object_file.write(f"{name.title()} visited today\n")