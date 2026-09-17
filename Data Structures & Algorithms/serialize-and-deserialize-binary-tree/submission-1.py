# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # 1,2,3,N,N,4 -- etc -- roughly linear time and space

        s = []
        def preorder(node):
            if not node:
                s.append("N")
                return
            
            s.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ','.join(s)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        i = 0
        chars = data.split(',')
    
        def build():
            nonlocal i
            if chars[i] == "N":
                i += 1
                return None

            node = TreeNode(int(chars[i]))
            i += 1
            node.left = build()
            node.right = build()

            return node
        
        return build()

        # to build
        # go left as much as we can (stop when we hit N)
        # go right 
