users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },

    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
}

# print("These are the current users: ") # This code prints the username and then values as a tuple for each.
# for user, username in users.items():
#     print(f"{user.title()}: ")
#     for deets in username.items():
#         print(f"\n{deets}")

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

eddie = {
    'first': 'eduardo',
    'last': 'corona',
    'location': 'napa valley',
}

lori = {
    'first': 'lorena',
    'last': ' lopez',
    'location': 'napa valley',
}

family = [eddie, lori]

for person in family:
    print(person)

sammi = {
    'type': 'dog',
    'owner': 'chepe',
}
luna = {
    'type': 'dog',
    'owner': 'juni',
}

cities = {
    'berlin': {
    'country': 'germany',
    'population': 3650000,
    'fact': 'a lot of trees',
    },

    'oia': {
    'country': 'greece',
    'population': 'less than 10k',
    'fact': 'located in island of Santorini',
    },

    'haifa': {
    'country': 'israel',
    'population': 279000,
    'fact': 'super dope city',
    },
}

for city, details in cities.items():
    print(f"\nCity: {city.title()} ")
    country = f"{details['country']}"
    population = f"{details['population']}"
    key_fact = f"{{details['fact']}}"
    print(f"Country: {country.title()}")
    print(f"Information: {population.title()} \nFact: {details['fact'].title()}")
    # for info in details:
    #     print(f"\n{info.title()}")