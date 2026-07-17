class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        l = len(nums)
        nums.sort()
        quads = set()

        # quadratic scan to fix all pairs
        for i in range(l):
            # skip to avoid exploring pairs that we alr explored
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, l):
                # skip to avoid exploring pairs that we alr explored
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                left, right = j+1, l-1
                # linear scan to find complementary pair 
                while left < right:
                    if left == right:
                        break

                    curr_quad = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_quad == target:
                        quads.add(tuple(sorted([nums[i], nums[j], nums[left], nums[right]])))
                        left += 1
                        right -= 1
                    elif curr_quad > target:
                        right -= 1
                    else:
                        left += 1

        return list(quads)  # O(n^3)