# main.py
from decision_logic import recommend_structure
from diagrams import get_diagram
from pseudocode import get_pseudocode
from examples import get_example

def ask_questions():
    print("=== GUIDED DATA STRUCTURE RECOMMENDATION SYSTEM ===\n")
    print("Answer the following questions with 'yes' or 'no':\n")

    answers = {}

    answers["random_access"] = input("Do you need fast random access by index? ").strip().lower()
    answers["middle_insert"] = input("Are insertions/deletions in the middle frequent? ").strip().lower()
    answers["fifo"] = input("Is FIFO (First-In-First-Out) processing required? ").strip().lower()
    answers["lifo"] = input("Is LIFO (Last-In-First-Out) processing required? ").strip().lower()
    answers["ordering_priority"] = input("Do you need ordering or priority for elements? ").strip().lower()
    answers["key_value"] = input("Are key→value lookups the main operation? ").strip().lower()
    answers["dynamic_size"] = input("Is the data size dynamic/unbounded? ").strip().lower()
    answers["prefix_search"] = input("Do you need prefix search on strings? ").strip().lower()
    answers["graph_relations"] = input("Are graph-like relationships present? ").strip().lower()
    answers["range_queries"] = input("Do you need range queries or sorted traversal? ").strip().lower()

    return answers


def main():
    answers = ask_questions()
    structure, reason = recommend_structure(answers)

    print("\n=== RECOMMENDATION ===")
    print("Best data structure:", structure)
    print("Reason:", reason)

    print("\n=== DIAGRAM ===")
    print(get_diagram(structure))

    print("\n=== PSEUDOCODE ===")
    print(get_pseudocode(structure))

    print("\n=== EXAMPLE ===")
    print(get_example(structure))

    print("\n=== END OF SYSTEM ===")

if __name__ == "__main__":
    main()

