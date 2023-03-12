def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease enter your name: ")
    print("Enter 'q' to quit")

    f_name = input("First Name: ")
    if f_name == 'q':
        break
    m_name = input("Middle Name (Type NA if none): ")
    if m_name == 'q':
        break 
    elif m_name == 'NA':
        pass
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    full_name = formatted_name = get_formatted_name(f_name, l_name, m_name)

print(full_name)