# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = float("-inf")

    def findMax(self, node: Optional[TreeNode]) -> int:
        if not node: return 0
        
        left_val = self.findMax(node.left) if node.left else 0
        right_val = self.findMax(node.right) if node.right else 0

        max_gain = max(
            node.val,
            node.val + left_val,
            node.val + right_val,
        )
        self.result = max(self.result, node.val + max(left_val, 0) + max(right_val, 0))
        return max_gain 
                   
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.findMax(root)
        return self.result