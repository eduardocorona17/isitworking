def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person
musician = build_person("Jimmi", "Hendrix", 27)
print(musician)
print(build_person("Edu", "Corona"))

teacher = {
    'first': 'Eduardo',
    'last': 'Corona',
    'details': {
    'hometown': 'Napa Valley',
    'age': 27,
    'degree': "masters",
    }
}
for key, value in teacher['details'].items():
    print(f"{key} {value}")

   