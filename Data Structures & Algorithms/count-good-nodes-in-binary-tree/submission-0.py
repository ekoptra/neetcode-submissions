# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traceGoodNodes(self, node: TreeNode, max_val: int) -> int:
        if not node: return 0
        
        left = self.traceGoodNodes(node.left, max(max_val, node.val))
        right = self.traceGoodNodes(node.right, max(max_val, node.val))
        
        return left + right + (1 if node.val >= max_val else 0)


    def goodNodes(self, root: TreeNode) -> int:
        return self.traceGoodNodes(root, root.val)