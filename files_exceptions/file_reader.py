# with open('files_exceptions/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

filename = 'files_exceptions/pi_digits.txt'
with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# for line in lines:
#     print(line.rstrip())
filename_2 = 'files_exceptions/learning_python.txt'
with open(filename_2) as file_object:
    cont = file_object.read()
print(cont.rstrip())

with open(filename_2) as file_ob:
    for line in file_ob:
        print(line)

with open(filename_2) as filesss:
    lines = filesss.readlines()

learn_string = ""
for line in lines:
    learn_string += line
print(f"{learn_string}")
print(len(learn_string))
