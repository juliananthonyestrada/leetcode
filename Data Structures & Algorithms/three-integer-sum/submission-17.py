class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            left = 0
            right = len(nums)-1
            while left < right:
                if i == left:
                    left += 1
                elif i == right:
                    right -= 1
                elif nums[left] + nums[right] == -nums[i]:
                    ans.add(tuple(sorted((nums[left], nums[right], nums[i]))))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return list(ans)