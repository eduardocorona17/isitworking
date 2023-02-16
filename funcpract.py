def desc_pet(animal_type, pet_name):
    """Display pet info"""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
# print(desc_pet("dog", "sammi"))
desc_pet("dog", "luna")
desc_pet("dog", "sammi")
# print(desc_pet)
desc_pet("cat", "yany")
def dif_animal(name, type='dog'):
    print(f"\nMy pet {type.title()} is named {name}")
dif_animal("Sami")

def make_shirt(size, text="I Love Python!"):
    print(f"My t-shirt size is {size} and it says {text}!")
make_shirt("Medium")
make_shirt("Large", "I hate Python")

def desc_city(city, country):
    print(f"{city.title()} is in {country.title()} and it is doooope!")
desc_city("Jerusalem", "Israel")
desc_city("York", "England")

def get_form_name(f_name, l_name, m_name=""):
    if m_name:
        full = f"{f_name} {m_name} {l_name}"
        
    else:
        full = f"{f_name} {l_name}"
    return full
print(get_form_name("Edu", "Corona", "Angel"))
print(get_form_name("Edu","Corona"))