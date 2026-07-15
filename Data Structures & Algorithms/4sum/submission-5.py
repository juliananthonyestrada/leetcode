class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # helper function to skip over indices of the currently fixed pair
        def get_valid_ptrs(i, j, left, right):
            if left == i:
                left += 1
            if left == j:
                left += 1
            if right == j:
                right -= 1
            if right == i:
                right -= 1
            return left, right
                
        l = len(nums)
        nums.sort()
        quads = set()

        # quadratic scan to fix all pairs
        for i in range(l):
            for j in range(i+1, l):
                left, right = 0, l-1

                # linear scan to find complementary pair 
                while left < right:
                    left, right = get_valid_ptrs(i, j, left, right)
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