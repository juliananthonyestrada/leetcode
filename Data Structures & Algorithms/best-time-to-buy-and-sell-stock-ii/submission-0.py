class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prof, prev_min = 0, prices[0]

        for curr_price in prices[1:]:
            # money can be made
            if curr_price > prev_min:
                prof += (curr_price - prev_min)
            
            prev_min = curr_price
        
        return prof