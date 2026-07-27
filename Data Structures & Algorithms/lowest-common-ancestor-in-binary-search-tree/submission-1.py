# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if the directions are diff then that is where they diverge
        if p.val == root.val or q.val == root.val:
            return root

        pdir, qdir = (p.val > root.val), (q.val > root.val)        

        if pdir == qdir:
            if pdir:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root