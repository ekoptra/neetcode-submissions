# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        srz_tree = ''
        if not root:
            return srz_tree

        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                srz_tree += "#"
                continue

            srz_tree += f"{node.val}#"
            q.extend([node.left, node.right])
            
        return srz_tree

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '': return None

        list_data = data.split("#")
        root = TreeNode(int(list_data[0]))
        
        q = collections.deque([root])
        i = 1
        while i < len(list_data) and q:
            node = q.popleft()
            val_left = list_data[i]

            if val_left != '':  
                node.left = TreeNode(int(val_left))
                q.append(node.left)
            
            i += 1
            if i >= len(list_data):
                break

            val_right = list_data[i]
            if val_right != '':
                node.right = TreeNode(int(val_right))
                q.append(node.right)
            i += 1

        return root













