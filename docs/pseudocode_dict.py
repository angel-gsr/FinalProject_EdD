# pseudocode_dict.py
PSEUDOCODE = {
"Static Array": """Procedure GET(A, index)
Precondition: 0 <= index < A.size
Return A[index]  // O(1)
""",
"Dynamic Array": """Procedure APPEND(A, value)
if A.size == A.capacity then
    resize to 2 * A.capacity  // O(n) occasionally, amortized O(1)
A[A.size] = value
A.size = A.size + 1
""",
"Linked List": """Procedure INSERT_FRONT(L, value)
new_node = Node(value)
new_node.next = L.head
L.head = new_node  // O(1)

Procedure DELETE(L, target)
traverse until target, update pointers // O(n)
""",
"Doubly Linked List": """Procedure INSERT_AFTER(node, value)
new = Node(value)
new.prev = node
new.next = node.next
node.next.prev = new
node.next = new  // O(1)
""",
"Queue": """Procedure ENQUEUE(Q, value)
Q.rear = (Q.rear + 1) mod Q.capacity
Q.array[Q.rear] = value
Q.size = Q.size + 1  // O(1)

Procedure DEQUEUE(Q)
if Q.size == 0 then error
value = Q.array[Q.front]
Q.front = (Q.front + 1) mod Q.capacity
Q.size = Q.size - 1
return value  // O(1)
""",
"Stack": """Procedure PUSH(S, value)
S.top = S.top + 1
S.array[S.top] = value  // O(1)

Procedure POP(S)
if S.top == -1 then error
value = S.array[S.top]
S.top = S.top - 1
return value  // O(1)
""",
"Heap": """Procedure HEAP_INSERT(H, value)
H.size = H.size + 1
H[H.size] = value
bubble up to restore heap property  // O(log n)

Procedure EXTRACT_MIN(H)
if H.size == 0 then error
min = H[1]
H[1] = H[H.size]
H.size = H.size - 1
HEAPIFY(1)  // O(log n)
return min
""",
"Hash Table": """Procedure PUT(T, key, value)
idx = hash(key) mod T.capacity
insert (key,value) into bucket idx (chain or probe)  // O(1) avg

Procedure GET(T, key)
idx = hash(key) mod T.capacity
search bucket for key, return value or NOT_FOUND  // O(1) avg
""",
"Trie": """Procedure INSERT(T, word)
node = T.root
for each char in word:
    if node.child[char] == null then create node
    node = node.child[char]
mark node as end-of-word  // O(len(word))

Procedure PREFIX_SEARCH(T, prefix)
node = traverse prefix
collect all words below node  // O(len(prefix) + results)
""",
"BST": """Procedure INSERT(node, value)
if node == null then return new Node(value)
if value < node.value then node.left = INSERT(node.left, value)
else node.right = INSERT(node.right, value)
return node  // O(h)
"""
}
