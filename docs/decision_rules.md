# Decision Rules
This document defines the deterministic logic used to map questionnaire answers to a final recommendation.  
Each rule includes a rationale explaining why the structure fits the selected constraints.

---

## Rule 1 — Array / Dynamic Array
**Conditions:**
- Random access = YES  
- Frequent middle insert/delete = NO  
- Data size static or moderately dynamic  

**Recommend:** Dynamic Array  
**Rationale:** Provides O(1) index access, simple memory layout, and amortized O(1) append.

---

## Rule 2 — Singly/Doubly Linked List
**Conditions:**
- Random access = NO  
- Frequent middle insert/delete = YES  
- Ordering not strongly required  

**Recommend:** Linked List  
**Rationale:** Insertions and deletions in the middle are O(1) when node references are available.

---

## Rule 3 — Stack
**Conditions:**
- LIFO behavior = YES  

**Recommend:** Stack  
**Rationale:** Supports push/pop operations in O(1); ideal for backtracking or recent-element access.

---

## Rule 4 — Queue
**Conditions:**
- FIFO behavior = YES  

**Recommend:** Queue  
**Rationale:** Ensures correct processing order for tasks, events, or workflows; operations are O(1).

---

## Rule 5 — Priority Queue / Heap
**Conditions:**
- Ordering = YES  
- Priority-based retrieval = YES  

**Recommend:** Heap  
**Rationale:** Guarantees O(log n) insertion and extraction of highest/lowest priority.

---

## Rule 6 — Binary Search Tree (BST)
**Conditions:**
- Ordered data required  
- Range queries needed  
- Not strictly priority-based  

**Recommend:** BST  
**Rationale:** Supports ordered traversal, range queries, and search operations in O(log n) average.

---

## Rule 7 — Hash Table
**Conditions:**
- Key→value lookup = YES  
- Ordering = NO  

**Recommend:** Hash Table  
**Rationale:** Offers O(1) average lookup and insertion, ideal when order does not matter.

---

## Rule 8 — Graph (Adjacency List or Matrix)
**Conditions:**
- Graph-like relationships present = YES  

**Recommend:** Graph Structure  
**Rationale:** Represents nodes and connections efficiently using adjacency lists or matrices.

---

## Rule 9 — Trie
**Conditions:**
- Prefix search required = YES  

**Recommend:** Trie  
**Rationale:** Specializes in prefix operations and supports O(length_of_string) lookup.

---

## Fallback Rule — Dynamic Array
**Conditions:**
- No strong specialization required  
- Data grows dynamically  

**Recommend:** Dynamic Array  
**Rationale:** Best general-purpose structure when no features strongly indicate another structure.
