# pseudocode.py
from pseudocode_dict import PSEUDOCODE
def get_pseudocode(structure):
    return PSEUDOCODE.get(structure, "Pseudocode not available for this structure.")
