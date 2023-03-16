

# print("Printing current models: ")
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design} ")
#     completed_models.append(current_design)
# print("\nThese designs have been printed: ")
# for model in completed_models:
#     print(f"{model.title()}")
unprinted_designs = ['phone chip', 'machine pendant', 'dodecahedron']
completed_models = []

# Modified code below:
def print_models(unprinted_models, completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing model: {current_designs}")
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(f"{completed_model}")

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
