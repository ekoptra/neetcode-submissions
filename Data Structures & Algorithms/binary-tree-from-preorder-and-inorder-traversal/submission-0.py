# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        i = 0
        p = 1
        after_remove = None

        while p < len(preorder):
            node = TreeNode(preorder[p])
            if after_remove is not None:
                after_remove.right = node
                stack.append(node)
                after_remove = None
            else:
                top_stack = stack[-1]
                top_stack.left = node
                stack.append(node)
        
            p += 1
            while stack and i < len(inorder) and stack[-1].val == inorder[i]:
                i += 1
                after_remove = stack.pop()
    
        return root