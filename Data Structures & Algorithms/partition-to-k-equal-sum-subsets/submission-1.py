class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0: return False

        groups = [0] * k
        amt = sum(nums)//k

        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if groups[j] + nums[i] <= amt:
                    groups[j] += nums[i]
                    if dfs(i+1):
                        return True
                    groups[j] -= nums[i]
                
                if groups[j] == 0:
                    break

            return False
        
        return dfs(0)