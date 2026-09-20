class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        sidelength = sum(matchsticks) // 4
        if sum(matchsticks) % 4 != 0: return False

        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= sidelength:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]       

                if sides[j] == 0:
                    break
            
            return False
        
        return dfs(0)