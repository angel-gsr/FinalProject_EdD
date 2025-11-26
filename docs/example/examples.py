# examples.py
EXAMPLES={
"Dynamic Array":"Ejemplo dinámico...",
"Linked List":"""
Example: Graph adjacency list implemented with linked lists

We represent cities as vertices in an array, and each city stores a linked list
of adjacent cities. Each edge node contains:
    - Index of adjacent vertex
    - Weight (distance)
    - Pointer to the next edge

Graph Example:
    [0] Atlanta      → (5, 800) → (6, 600)
    [1] Austin       → (3, 200) → (5, 160)
    [2] Chicago      → (4, 1000)
    [3] Dallas       → (1, 200) → (2, 900) → (4, 780)
    [4] Denver       → (0, 1400) → (2, 1000)
    [5] Houston      → (0, 800)
    [6] Washington   → (0, 600) → (3, 1300)

Where each tuple is:
    (adjacent_vertex_index, weight)

This structure allows:
    - Fast traversal of all neighbors of a vertex
    - Efficient insertions (adding an edge)
    - Dynamic edge list growth

It is a classic example of using linked lists to represent sparse graphs.
"""
}",
"BST":"Ejemplo BST...",
"Graph":"Ejemplo grafo..."
}
def get_example(structure):
    return EXAMPLES.get(structure,"No hay ejemplo.")
