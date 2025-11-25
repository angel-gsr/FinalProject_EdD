# decision_logic.py

def recommend_structure(a):

    if a["random_access"] == "yes":
        return "Dynamic Array", "Fast random access required → arrays are optimal."

    if a["middle_insert"] == "yes":
        return "Linked List", "Frequent middle insertions → linked list fits best."

    if a["fifo"] == "yes":
        return "Queue", "FIFO processing required → queue selected."

    if a["lifo"] == "yes":
        return "Stack", "LIFO processing required → stack selected."

    if a["ordering_priority"] == "yes":
        return "Heap", "Elements need ordering or priority → heap/priority queue is ideal."

    if a["key_value"] == "yes":
        return "Hash Table", "Key→value lookups dominate → hash table recommended."

    if a["prefix_search"] == "yes":
        return "Trie", "Prefix-based string search → Trie is appropriate."

    if a["graph_relations"] == "yes":
        return "Graph", "Graph-like relationships detected → use graph structure."

    if a["range_queries"] == "yes":
        return "BST", "Range queries / sorted traversal → BST or balanced tree required."

    if a["dynamic_size"] == "yes":
        return "Dynamic Array", "Dynamic/unbounded size → dynamic array is suitable."

    return "Linked List", "Default: flexible structure with low overhead."
