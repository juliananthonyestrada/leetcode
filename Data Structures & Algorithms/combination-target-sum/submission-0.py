class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr_sum, arr, num):
            # over the target -> stop exploring this path
            if curr_sum > target:
                return
            # found the target -> store this arr
            elif curr_sum == target:
                lst = sorted(arr)
                if lst not in res:
                    res.append(lst)
            # under the target -> explore all paths now 
            else:
                for n in nums:
                    arr.append(n)
                    curr_sum += n
                    dfs(curr_sum, arr, n)
                    arr.pop()
                    curr_sum -= n
        
        dfs(0, [], nums[0])

        return res