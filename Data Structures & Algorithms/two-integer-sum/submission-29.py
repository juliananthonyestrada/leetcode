class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapp = {num : i for i, num in enumerate(nums)}

        print(mapp)

        for i, num in enumerate(nums):
            if target - num in mapp and i != mapp[target-num]:
                return sorted([i, mapp[target-num]])
        