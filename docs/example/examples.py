# examples.py
EXAMPLES={
"Dynamic Array":"Ejemplo dinámico...",
"Linked List":"Ejemplo lista...",
"BST":"Ejemplo BST...",
"Graph":"Ejemplo grafo..."
}
def get_example(structure):
    return EXAMPLES.get(structure,"No hay ejemplo.")
