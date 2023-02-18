coll = {
    'Etienne': {
    'Title': 'Software marketing',
    'Salary': 120000,
    'Location': 'Paris, France',
    },
   'Matthias': {
    'Title': "Police Officer",
    'Salary': 80000,
    'Location': 'Ansbach, Germany'
    },
}

print(f"Here are the details for employee: ")
# print(f"{coll}")
for c, deets in coll.items():
    # print(f" {c}: \n{deets}")
    print(f"{c}:")
    details = f"{deets['Title']} \n\t'Salary': {deets['Salary']}"
    print(f"\t{details}")
    loc = f"\t{deets['Location']}"
    print(f"{loc}")

    