class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(curr_sum, index, arr):
            print(curr_sum, index, arr)
            if curr_sum == target:
                res.append(arr.copy())
            for i in range(index+1, len(candidates)):
                if i != 0 and i > index+1 and candidates[i] == candidates[i-1]:
                    continue
                if curr_sum + candidates[i] <= target:
                    arr.append(candidates[i])
                    helper(curr_sum + candidates[i], i, arr)
                    arr.pop()

        helper(0, -1, [])

        return res