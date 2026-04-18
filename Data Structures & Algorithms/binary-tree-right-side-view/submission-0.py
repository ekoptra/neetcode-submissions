# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([])

        res = []
        if root: queue.append(root)

        while len(queue) != 0:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                
                if i == (queue_len - 1):
                    res.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res