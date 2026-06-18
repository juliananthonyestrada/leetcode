class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)//2
        freq = {}

        # create a freq map
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
            if freq[num] > n:
                    return num
        # in creating, if we encounter a number that appears more than n/2 times then return 
