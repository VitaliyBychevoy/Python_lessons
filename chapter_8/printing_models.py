#Список моделей, которые необходимо напечатать
import printing_function as pf

"""
def print_models(unprinted_designs , completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}.")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"{completed_model}")


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models )
"""

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)