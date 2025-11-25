# diagrams.py
from diagrams_ascii import DIAGRAMS
def get_diagram(structure):
    return DIAGRAMS.get(structure, "No diagram available for this structure.")
