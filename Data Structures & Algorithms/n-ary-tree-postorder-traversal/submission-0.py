"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.result = []
    
    def traverse(self, node):
        if not node: return

        for child in node.children:
            self.traverse(child)
        
        self.result.append(node.val)

    def postorder(self, root: 'Node') -> List[int]:
        self.traverse(root)
        return self.result