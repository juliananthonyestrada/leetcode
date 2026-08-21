class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        i, start, tank, visited = -1, 0, 0, 0
        gas_len = len(gas)

        while start < gas_len:
            start = (i + 1)
            i = start

            # attempt circuit
            while visited != gas_len:
                curr_station = i % gas_len
                tank += gas[curr_station]

                # we can get to the next station
                if tank >= cost[curr_station]:
                    tank -= cost[curr_station]
                    visited += 1
                    i += 1
                # this starting point fails
                else:
                    break
            
            if visited == gas_len:
                return start
            else:
                tank = 0
                visited = 0



        return -1