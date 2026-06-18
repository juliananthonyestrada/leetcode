class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Quadratic approach 

        for i in range(len(nums)):
            for j in range(len(nums)):
                # When indices are equivalent, skip to next iteration 
                if i == j:
                    continue
                # Indices are not equal so we check 
                if nums[i] + nums[j] == target:
                    return sorted([i, j])