filename = 'files_exceptions/programming.txt'
#These lines 'write' into a file
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming. I think Python is cool.\n")
#     file_object.write("I should have leaned JS and React first though lol.\n")

#These files 'append' onto a file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")