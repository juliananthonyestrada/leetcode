class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr_sum, arr, idx):
            # over the target -> stop exploring this path
            if curr_sum > target:
                return
            # found the target -> store this arr
            elif curr_sum == target:
                res.append(arr.copy())
            # under the target -> explore all paths  
            else:
                for i in range(idx, len(candidates)):
                    arr.append(candidates[i])
                    curr_sum += candidates[i]
                    dfs(curr_sum, arr, i)
                    curr_sum -= candidates[i]
                    arr.pop()

        dfs(0, [], 0)

        return res