class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # guarantees a solution
        if sum(gas) < sum(cost):
            return -1

        res, tank = 0, 0
        for strt in range(len(gas)):
            # attempt to get the next station
            tank += gas[strt]
            tank -= cost[strt]
            # failed
            if tank < 0:
                tank = 0
                res = strt + 1
        
        return res