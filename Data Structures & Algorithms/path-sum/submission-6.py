# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # edge case: empty tree
        if not root:
            return False

        def dfs(node, curr_sum):
            # base case 1: we are at a dead node
            if not node:
                return False
            # valid path: add the curr node val to the curr sum
            curr_sum += node.val
            # at a leaf: check if valid path
            if not node.left and not node.right:
                return curr_sum == targetSum
            # not at leaf yet: keep checking
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
            # explored entire subtrees and no we backtrack 
            curr_sum -= node.val

        return dfs(root, 0)