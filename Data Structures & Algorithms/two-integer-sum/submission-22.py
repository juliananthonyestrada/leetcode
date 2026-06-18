class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Hash map approah 
        # num:diff
        hash_map = {}

        # Add each element and its index to the hash map
        for i, num in enumerate(nums):
            if (target - num) in hash_map.keys() and i != hash_map[target-num]:
                return sorted([i, hash_map[target - num]])
            else:
                hash_map[num] = i
        
        