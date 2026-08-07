# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def search(root1, root2):
            # fell off tree - no valid pair
            if not (root1 and root2):
                return False

            curr_sum = root1.val + root2.val

            if curr_sum == target:
                return True
            elif target < curr_sum:
                return search(root1, root2.left) or search (root1.left, root2)
            else:
                return search(root1, root2.right) or search (root1.right, root2)
        
        return search(root1, root2)
