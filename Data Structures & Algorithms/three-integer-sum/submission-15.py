class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # we run two sum n times for each number in the list

        l = len(nums)
        triplets = set()
        nums.sort()

        for i in range(l):
            target = -(nums[i])

            left, right = 0, l-1

            # search for pair to complete the triplet
            while left < right:
                # skip curr idx
                if left == i:
                    left += 1
                if right == i:
                    right -= 1
                if left == right:
                    break

                pair = nums[left] + nums[right]
                
                if pair == target:
                    trip = tuple(sorted((nums[i], nums[left], nums[right])))
                    if trip not in triplets:
                        triplets.add(trip)
                    left += 1
                    right -= 1
                elif pair > target:
                    right -= 1
                else:
                    left += 1

        return list(triplets)