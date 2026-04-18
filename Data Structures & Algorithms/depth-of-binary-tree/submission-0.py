# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traceDepth(self, node, depth):
        if not node: return depth

        max_left = self.traceDepth(node.left, depth + 1)
        max_right = self.traceDepth(node.right, depth + 1)
        return max(max_left, max_right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traceDepth(root, 0)