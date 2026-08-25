class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prof = 0

        prev_min = prices[0]

        for curr_price in prices[1:]:
            if curr_price > prev_min:
                prof = max(prof, curr_price - prev_min)
            else:
                prev_min = curr_price
                
        return prof