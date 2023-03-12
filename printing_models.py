unprinted_designs = ['phone chip', 'machine pendant', 'dodecahedron']
completed_models = []

print("Printing current models: ")
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design} ")
    completed_models.append(current_design)
print("\nThese designs have been printed: ")
for model in completed_models:
    print(f"{model.title()}")
