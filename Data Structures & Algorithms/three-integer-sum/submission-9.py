class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        j, k = len(nums)-1, len(nums)-2

        # select current idx and look for pairs that satisfy
        for i in range(len(nums)):
            
            # create a search array excluding current element
            temp = nums[0:i] + nums[i+1:]

            left, right = 0, len(temp)-1
            target = -(nums[i])

            # search for valid pair
            while left < right:
                # valid triple
                if left != right and left != i and right != i and nums[left] + nums[right] == target:
                    if sorted([nums[left], nums[right], nums[i]]) not in res:
                        res.append(sorted([nums[left], nums[right], nums[i]]))
                    left += 1
                    right -= 1
                # sum is greater - make smaller
                elif nums[left] + nums[right] > target:
                    right -= 1
                # sum is lesser - make greater
                else:
                    left += 1
        
        return res