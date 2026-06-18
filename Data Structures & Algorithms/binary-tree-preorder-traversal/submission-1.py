# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res, call_stack = [], []
        curr = root

        while curr or call_stack:
            # immediately visit and explore all the way to the left
            while curr:
                res.append(curr.val)
                call_stack.append(curr)
                curr = curr.left
            # go back up to parent and then navigate to right child
            curr = call_stack.pop().right

        return res
