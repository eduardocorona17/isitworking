def build_person(first, last):
    person = {'first': first, 'last': last}
    return person
musician = build_person("Jimmi", "Hendrix")
print(musician)
print(build_person("Edu", "Corona"))