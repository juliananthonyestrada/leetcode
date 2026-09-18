class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        prof = 0

        while r < len(prices):
            # money can be made
            if prices[r] > prices[l]:
                prof = max(prof, prices[r]-prices[l])
            # wait for better day
            else:
                l = r
            r += 1
        
        return prof