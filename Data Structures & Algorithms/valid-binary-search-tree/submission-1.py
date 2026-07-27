# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root
    
    def findMax(self, root):
        while root and root.right:
            root = root.right
        return root

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        if root.left and root.val <= self.findMax(root.left).val: 
            return False
        elif root.right and root.val >= self.findMin(root.right).val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
