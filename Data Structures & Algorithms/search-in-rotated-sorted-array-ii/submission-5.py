class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # l, m, r

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            # we dont know
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            # left half is sorted
            elif nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right half is sorted
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return False
