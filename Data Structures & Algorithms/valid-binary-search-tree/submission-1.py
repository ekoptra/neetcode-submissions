# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = True
        self.current_val = float('-inf')

    def inOrderCheck(self, node: Optional[TreeNode]):
        if not node: return
        
        self.inOrderCheck(node.left)
        if node.val <= self.current_val: 
            self.result = False
            return
        else:
            self.current_val = node.val
        self.inOrderCheck(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inOrderCheck(root)
        return self.result
