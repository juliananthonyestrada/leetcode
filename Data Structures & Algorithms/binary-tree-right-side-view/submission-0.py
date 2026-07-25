# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                curr = queue.popleft()
                print(curr)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return res