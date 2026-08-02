from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

nodes = [Node(3), Node(7), Node(4), Node(5)]
for a, b in zip(nodes, nodes[1:]):
    a.next = b
random_index = [None, 3, 0, 1]
for i, j in enumerate(random_index):
    nodes[i].random = nodes[j] if j is not None else None
head = nodes[0]

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None:None}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new[current.next]
            copy.random = old_to_new[current.random]
            current = current.next
        return old_to_new[head]

        
