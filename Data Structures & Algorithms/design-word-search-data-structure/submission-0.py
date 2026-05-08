class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()

            curr = curr.children[w]
        
        curr.is_word = True

    def find(self, word: str, i: int, curr: Node) -> bool:
        if i >= len(word):
            return curr.is_word
                
        if word[i] != '.':
            if word[i] not in curr.children:
                return False
            else:
                return self.find(word, i+1, curr.children[word[i]])
        
        for c in curr.children:
            if self.find(word, i+1, curr.children[c]):
                return True

        return False

    def search(self, word: str) -> bool:
        return self.find(word, 0, self.root)