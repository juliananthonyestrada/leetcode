class Solution:
    def trap(self, height: List[int]) -> int:
        
        # amt of water at each position is limited by 2 things:
            # - the height of the building at the curr position
            # - the size of the smaller building adjacent to it (left or right)
        
        water = 0
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
    
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(height[l], lmax)
                water += lmax - height[l]
            else:
                r -= 1
                rmax = max(height[r], rmax)
                water += rmax - height[r]

        return water