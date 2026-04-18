# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.k = None
        self.result = None

    def inorderTrace(self, node: Optional[TreeNode]) -> int:
        if not node: return

        self.inorderTrace(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self.inorderTrace(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.inorderTrace(root)
        return self.result