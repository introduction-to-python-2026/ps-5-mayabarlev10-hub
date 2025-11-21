
def split_before_uppercases(formula):
    word = ""
    new_formula = []
    if not formula:
      return []
    word = formula [0]
    index = 1
    while index < len(formula):
        if formula[index].isupper() == False:
            word+=formula[index]
            index+=1
        else: 
            new_formula.append(word)
            word = formula[index]
            index+=1
    new_formula.append(word)
    return new_formula

def split_at_digit(formula):
    word = ""
    num = ""
    for split in formula:
        if split.isdigit():
            num+=split
        else:
            word+=split
    if num == "":
    num = "1"
    num_int = int(num)
    return word , num_int

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    count_atoms_in_molecule = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        
        count_atoms_in_molecule[atom_name] = atom_count
        # Step 2: Update the dictionary with the atom name and count
    return count_atoms_in_molecule
    # Step 3: Return the completed dictionary




def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
