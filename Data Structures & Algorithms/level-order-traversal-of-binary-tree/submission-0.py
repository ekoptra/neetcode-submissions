# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        queue = [root]
        result = []

        while queue:
            temp = []
            temp_queue = []
            for q in queue:
                temp.append(q.val)
                if q.left:
                    temp_queue.append(q.left)
                if q.right:
                    temp_queue.append(q.right)
            if len(temp) > 0:
                result.append(temp)
            queue = temp_queue

        return result