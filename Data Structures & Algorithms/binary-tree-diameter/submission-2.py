# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.cache = {}
        self.max_diameter = 0

    def traceDepth(self, node):
        if not node: return 0

        if node in self.cache:
            return self.cache[node]
        
        left = self.traceDepth(node.left)
        right = self.traceDepth(node.right)

        self.cache[node] = max(left, right) + 1
        self.max_diameter = max(self.max_diameter, left + right)

        return self.cache[node]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traceDepth(root)
        return self.max_diameter
