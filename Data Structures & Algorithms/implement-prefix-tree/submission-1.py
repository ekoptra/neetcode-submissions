class Node:
    def __init__(self, char, is_last):
        self.char = char
        self.is_last = is_last
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.head = Node('', False)        

    def insert(self, word: str) -> None:
        head = self.head
        i = 0
        while i < len(word):
            is_last = i == len(word) - 1
            if word[i] in head.children:
                head = head.children[word[i]]
                if not head.is_last:
                    head.is_last = is_last
            else:
                new_head = Node(word[i], is_last)
                head.children[word[i]] = new_head
                head = new_head
            i += 1
    
    def findLastNode(self, word) -> Node:
        head = self.head
        for w in word:
            if w not in head.children:
                return None
            head = head.children[w]
        return head

    def search(self, word: str) -> bool:
        last_node = self.findLastNode(word)
        if last_node is None:
            return False
        return last_node.is_last

    def startsWith(self, prefix: str) -> bool:
        last_node = self.findLastNode(prefix)
        return last_node is not None
        
        