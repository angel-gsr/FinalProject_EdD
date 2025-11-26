# Decision Questions
This document lists the final set of questions used by the Guided Decision System.  
Each question targets a specific behavioral requirement or constraint that helps discriminate between data structures.

---

## 1. Do you need fast random access by index?
**Why:** Distinguishes arrays/dynamic arrays from linked lists and other pointer-based structures.

---

## 2. Will you frequently insert or delete elements in the middle of the collection?
**Why:** Strong indicator for linked lists; arrays perform poorly here due to shifting.

---

## 3. Are key→value lookups the primary operation you need?
**Why:** Identifies hash tables, which offer average O(1) key lookup.

---

## 4. Do you need the elements to remain ordered (ascending, descending, or by priority)?
**Why:** Narrows the choice to BSTs, heaps/priority queues, or sorted lists.

---

## 5. Do you need FIFO (first-in, first-out) processing?
**Why:** Characteristic of queues.

---

## 6. Do you need LIFO (last-in, first-out) processing?
**Why:** Characteristic of stacks.

---

## 7. Will the data size grow dynamically without a known upper bound?
**Why:** Helps distinguish between static arrays and dynamic/linked structures.

---

## 8. Are graph-like relationships present (nodes with multiple connections)?
**Why:** Indicates adjacency lists/matrices or general graph structures.

---

## 9. Do you need efficient prefix search (e.g., autocomplete or dictionary-like prefix checks)?
**Why:** Points to tries, which specialize in prefix-based operations.

---

## 10. Do you need efficient range queries or ordered traversal?
**Why:** Helps distinguish BSTs (inorder traversal) from hash tables (unordered).

---

## 11. Do you need priority-based retrieval (always pick the highest or lowest priority element)?
**Why:** Indicates heaps or priority queues.

---

## 12. Do you need to store unique keys with potentially fast lookup and insertion?
**Why:** Further reinforces hash table suitability.
