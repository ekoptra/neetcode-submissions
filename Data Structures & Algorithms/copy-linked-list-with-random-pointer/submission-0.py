"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {}
        dummy = Node(0)
        cur = dummy

        while head:
            new_node = store.get(head, Node(head.val))            
            store[head] = new_node

            next_random = head.random
            if next_random:
                random_node = store.get(next_random, Node(next_random.val))
                new_node.random = random_node
                store[next_random] = random_node

            cur.next = new_node
            cur = cur.next
            head = head.next

        return dummy.next