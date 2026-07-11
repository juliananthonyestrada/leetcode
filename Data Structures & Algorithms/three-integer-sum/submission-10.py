class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # we run two sum n times for each number in the list

        l = len(nums)
        triplets = set()
        nums.sort()

        for i in range(l):
            search_space = nums[:i] + nums[i+1:]

            target = -(nums[i])

            left, right = 0, l-2

            while left < right:
                pair = search_space[left] + search_space[right]
                if pair == target:
                    trip = tuple(sorted((nums[i], search_space[left], search_space[right])))
                    if trip not in triplets:
                        triplets.add(trip)
                    left += 1
                    right -= 1
                elif pair > target:
                    right -= 1
                else:
                    left += 1

        return list(triplets)