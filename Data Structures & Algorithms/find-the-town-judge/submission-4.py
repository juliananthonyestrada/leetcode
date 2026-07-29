class Solution:
    # following someone disqualifies you from being the judge
    # the judge would have a score of n-1
    # followed by n-1 people (+n-1) and follows 0 (-0)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        score = [0] * (n+1)

        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        
        for i in range(len(score)):
            if score[i] == n-1:
                return i
        
        return -1
        
