# FinalProject_EdD

📘 Guided Data Structure Recommendation System

This project is an interactive Python-based system that guides the user through a series of questions to determine the most suitable data structure for a given use case.
The tool also provides:

A visual diagram of the recommended structure

A short pseudocode template

A practical usage example

It is designed as a final project for a Data Structures course, integrating decision logic, diagrams, pseudocode generation, and examples into a single console application.

🚀 Features

✅ Interactive Q&A system
Guides the user with yes/no questions to determine requirements.

✅ Automatic recommendation
Chooses the best-fitting data structure based on user needs:

Array

Linked List

Stack

Queue

Hash Table

Binary Tree

Graph

✅ Visual ASCII diagrams
Provides a quick structural representation.

✅ Pseudocode generation
Shows how the structure is typically implemented or used.

✅ Practical examples
Each structure includes a real-world usage demonstration.

📂 Project Structure
Final_Project_ESTRUCTURASD/
│
├── main.py               # Entry point of the system
├── decision_logic.py     # Handles the recommendation rules
├── diagrams.py           # ASCII diagrams of each structure
├── diagrams_ascii.py     # Alternate diagram set (if needed)
├── pseudocode.py         # Pseudocode generator
├── pseudocode_dict.py    # Pseudocode dictionary helper
├── examples.py           # Real-world examples for each structure

▶️ How to Run
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Run the application
python3 main.py


You will be prompted with questions such as:

Do you need fast random access by index? (yes/no)
Are insertions/deletions in the middle frequent? (yes/no)
Is FIFO processing required? (yes/no)
...


The program will then produce:

✔ A recommended data structure

✔ Diagram

✔ Pseudocode

✔ Example

📊 Example Output
=== RECOMMENDED DATA STRUCTURE ===
Stack

=== DIAGRAM ===
| A | → | B | → | C |  (top)

=== PSEUDOCODE ===
push(element):
    ...

=== EXAMPLE ===
Used for undo/redo operations in editors.

🧠 Purpose of the Project

This project demonstrates:

Problem analysis through a decision tree

Clear mapping between requirements and data structures

Organization of modular Python code

Ability to document, diagram, and explain chosen algorithms

It is ideal for educational use or as a reference for beginners learning how to select data structures.

📜 License

This project is licensed under the MIT License, allowing free use, modification, and distribution.
