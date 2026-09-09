# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def max_path(node):
            if not node:
                return 0
            
            nonlocal res

            left = max_path(node.left)
            right = max_path(node.right)

            mp = max(node.val, node.val + left + right, node.val + left, node.val + right)
            res = max(res, mp)
            
            return max(node.val, node.val + left, node.val + right)
        
        max_path(root)
        return res

        # let mp = maxpath
        # node could be in path or not
        # left = mp(node.left)
        # right = mp(node.right)
        # mp(node) = max(node + left + right, left, right)