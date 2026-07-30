# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            # fell off
            if not node:
                return None

            # at leaf
            if not (node.left or node.right):
                if node.val == target:
                    return None
                else:
                    return node
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # at leaf
            if not (node.left or node.right):
                if node.val == target:
                    return None
                else:
                    return node

            return node

        return dfs(root)