class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # eat all banans in <= h hours

        # we have an eating rate k 
        # in 1 hour we can eat at most k bananas
        # from a single pile
        # we must eat all of the bananas in all 
        # of the piles in <= h hours 

        # lower bound = 1 -> we cant eat less than 1 banana per pile
        # upper bound = max(piles) -> why eat more bananas than there are in any given pile

        def ate_bananas(eating_rate: int):
            needed_hours = 0

            for p in piles:
                needed_hours += math.ceil(p / eating_rate)
                
            return needed_hours <= h


        lower, upper = 1, max(piles)

        while lower < upper:
            eating_rate = (lower + upper) // 2
            # valid eating rate -> try to decrease
            if ate_bananas(eating_rate):
                upper = eating_rate
            # invalid eating rate -> increase
            else:
                lower = eating_rate + 1


        return upper