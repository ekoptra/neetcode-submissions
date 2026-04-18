class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapper = {}
        self.head = None
        self.end = None
    
    def get(self, key: int) -> int:
        node = self.mapper.get(key)
        if node is None:
            return -1
        
        if self.end == node:
            return node.val
        
        if node == self.head and node.next:
            self.head = node.next

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.end.next = node
        node.prev = self.end
        node.next = None
        self.end = node
    
        return node.val
        
    def put(self, key: int, value: int) -> None:
        node = self.mapper.get(key)
        if node is not None:
            node.val = value
            self.get(key)
        else:
            if self.capacity == 0:
                node_del = self.head
                if self.head.next:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.head = self.end = None
                del self.mapper[node_del.key]
            else:
                self.capacity -= 1

            node = Node(key, value, self.end)
            if self.end is not None:
                self.end.next = node
            self.end = node
            
            if self.head is None:
                self.head = node
            
            self.mapper[key] = node
                

