class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # no ships in this region - don't search anymore
        if (bottomLeft.x > topRight.x 
            or bottomLeft.y > topRight.y
            or (not sea.hasShips(topRight, bottomLeft))):
            return 0
        elif (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y):
            return 1
        # at least 1 ship, search for more
        else:
            mid_width = abs(bottomLeft.x - topRight.x) // 2
            mid_length = abs(bottomLeft.y - topRight.y) // 2

        return (
            # bottom left
            self.countShips(sea, Point(bottomLeft.x + mid_width, bottomLeft.y + mid_length), Point(bottomLeft.x, bottomLeft.y)) +
            # top right
            self.countShips(sea, Point(topRight.x, topRight.y), Point(bottomLeft.x + mid_width + 1, bottomLeft.y + mid_length + 1)) +
            # bottom right
            self.countShips(sea, Point(topRight.x, bottomLeft.y + mid_length), Point(bottomLeft.x + mid_width + 1, bottomLeft.y)) +
            # top left
            self.countShips(sea, Point(bottomLeft.x + mid_width, topRight.y), Point(bottomLeft.x, bottomLeft.y + mid_length + 1))
            )