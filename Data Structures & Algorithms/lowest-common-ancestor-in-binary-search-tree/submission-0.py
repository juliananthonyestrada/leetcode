# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # to find all ancestors of a node we simply travel from the root to that node
        # and add all nodes in the path to an array
        # these are the ancestors

        def ancestry(root, target, arr):
            if not root:
                return arr
            
            arr.append(root)
            
            if target == root.val:
                return arr
            elif target > root.val:
                return ancestry(root.right, target, arr)
            else:
                return ancestry(root.left, target, arr)

        q_ancestors = ancestry(root, q.val, [])
        p_ancestors = ancestry(root, p.val, [])

        for i in range(min(len(q_ancestors), len(p_ancestors))-1, -1, -1):
            if q_ancestors[i].val == p_ancestors[i].val:
                return q_ancestors[i]
