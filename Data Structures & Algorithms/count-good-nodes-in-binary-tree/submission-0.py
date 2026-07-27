# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, curr_max):
            if not node:
                return 0

            if node.val >= curr_max:
                curr_max = node.val
                return 1 + dfs(node.left, curr_max) + dfs(node.right, curr_max)
            else:
                return dfs(node.left, curr_max) + dfs(node.right, curr_max)
                    
        
        return dfs(root, root.val)
        
        # dfs to explore all paths
        # track curr max
        # if node.val < curr_max:
            # do not contribute
        # else:
            # increment