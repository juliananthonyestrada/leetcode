# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
    
        def build(pre, inn):
            if not pre:
                return None
            r = pre[0]
            idx = inn.index(r)
            root = TreeNode(val=r)
            root.left = build(pre[1:idx+1], inn[0:idx])
            root.right = build(pre[idx+1:], inn[idx+1:])
            return root
        

        return build(preorder, inorder)

            