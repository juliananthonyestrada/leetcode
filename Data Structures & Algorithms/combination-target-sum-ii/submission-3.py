class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        l = len(candidates)
        candidates.sort()

        def dfs(arr, curr_sum, idx):

            if curr_sum == target:
                res.append(arr.copy())
                return
            elif curr_sum > target:
                return
            for i in range(idx, l):
                if i != idx and candidates[i] == candidates[i-1]:
                    continue
                curr_sum += candidates[i]
                arr.append(candidates[i])
                dfs(arr, curr_sum, i+1)    
                arr.pop()
                curr_sum -= candidates[i]

        dfs([], 0, 0)

        return res 