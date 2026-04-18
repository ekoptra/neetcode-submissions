# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.cache = {}

    def traceDepth(self, node):
        if not node: return 0

        max_left = self.traceDepth(node.left) + 1
        max_right = self.traceDepth(node.right) + 1
        return max(max_left, max_right)

    def trace(self, node):
        if not node: return 0

        if node in self.cache:
            return self.cache[node]

        left = self.traceDepth(node.left)
        right = self.traceDepth(node.right)

        self.cache[node] = left + right

        return self.cache[node]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return max(self.trace(root), self.trace(root.left), self.trace(root.right))



