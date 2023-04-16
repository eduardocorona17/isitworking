print("Enter first number to add.")
print("Press 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond num: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("The input was a string, please input an integer.")
    else:
        print(answer)