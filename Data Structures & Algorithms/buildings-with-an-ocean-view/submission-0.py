class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        curr_max = heights[-1]
        res = [len(heights)-1]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > curr_max:
                curr_max = heights[i]
                res.append(i)
        
        res.reverse()
        return res