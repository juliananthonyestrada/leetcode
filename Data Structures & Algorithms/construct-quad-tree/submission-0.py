"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def identical_quadrants(grid: List[List[int]]) -> bool:
            n = len(grid)
            mid = n // 2

            top_left = [row[0:mid] for row in grid[0:mid]]
            top_right = [row[mid:n] for row in grid[0:mid]]
            bot_left = [row[0:mid] for row in grid[mid:n]]
            bot_right = [row[mid:n] for row in grid[mid:n]]
            
            # Leaf: every cell in this region has the same value
            if all(cell == grid[0][0] for row in grid for cell in row):
                return Node(grid[0][0] == 1, True)
            
            n = n // 2
            topleft = identical_quadrants(top_left)
            topright = identical_quadrants(top_right)
            bottomleft = identical_quadrants(bot_left)
            bottomright = identical_quadrants(bot_right)

            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return identical_quadrants(grid)


        # look at current grid
        # are all four quadrants identical
            # yes, curr node is leaf, val = 0 or 1 accordingly
            # no, curr node is not a leaf, set val to any value and recurse over its 4 children by subdividing the matrix into 4 again