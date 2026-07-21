# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # inserting the first element
        if not root:
            root = TreeNode(val=val, left=None, right=None)
            return root

        def insert(root, val, parent):
            # found insertion spot
            if not root:
                new = TreeNode(val=val, left=None, right=None)
                if parent.val > val:
                    parent.left = new
                else:
                    parent.right = new
            else:
                if val > root.val:
                    insert(root.right, val, root)
                else:
                    insert(root.left, val, root)
            
        insert(root, val, None)

        return root
