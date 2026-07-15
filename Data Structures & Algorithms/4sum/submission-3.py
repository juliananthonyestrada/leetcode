class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # fix a pair and then among the remaining elements search for a pair
        l = len(nums)
        nums.sort()
        quads = set()
        print(nums)
        for i in range(l):
            for j in range(i+1, l):
                
                p1, p2 = nums[i], nums[j]
                pair = p1 + p2

                left, right = 0, l-1

                # linear scan to find complementary pair 
                while left < right:
                    if left == i:
                        left += 1
                    if left == j:
                        left += 1
                    if right == j:
                        right -= 1
                    if right == i:
                        right -= 1
                    if left == right:
                        break

                    # at this point we have valid ptrs
                    curr_quad = pair + nums[left] + nums[right]
                    if curr_quad == target:
                        quads.add(tuple(sorted([p1, p2, nums[left], nums[right]])))
                        left += 1
                        right -= 1
                    elif curr_quad > target:
                        right -= 1
                    else:
                        left += 1

        return list(quads)        