dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
# for dimen in dimensions:
#     print(dimen)
print("Our original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

buffet = ('Pizza', 'Pasta', 'Sandwhiches', 'Beer', 'Liquor')
print("Here are the items we offer: ")
for food in buffet:
    print(f"{food}")
buffet = ("Pizza", "Pasta", "Sandwhiches", "Apple Juice", "Milk")
print("We lost our liquor license: ")
for food in buffet:
    print(f"{food}")