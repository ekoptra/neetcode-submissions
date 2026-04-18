# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = True

    def traceTree(self, node: Optional[TreeNode]) -> int:
        if not node: return 0
        
        left = self.traceTree(node.left)
        right = self.traceTree(node.right)

        self.result = self.result and (abs(left - right) <= 1)

        return max(left, right) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.traceTree(root)
        return self.result