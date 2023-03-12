def build_person(first_name, last_name, age=None):
    if age:
        person = {'first': first_name, 'last': last_name, 'age': age}
    else:
        person = {'first': first_name, 'last': last_name}
    return person
print(build_person("Eduardo", "Corona", 27))
dude = build_person('Henlo', 'Lilpapabear')
print(dude)