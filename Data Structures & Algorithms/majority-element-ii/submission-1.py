class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        threshold = len(nums) // 3
        res = set()

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
            if freq[num] > threshold:
                    res.add(num)

        return list(res)