class Solution:

    def xor_total(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 0 is the identity element for xor
        running = 0

        for num in nums:
            running ^= num
        
        return running

    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0

        def subsets(idx, sub):
            nonlocal res

            # last element in array - does not track size of sub - we can reach the last element w all no decisions
            if idx == len(nums):
                res += self.xor_total(sub)
                return
            
            # take
            sub.append(nums[idx])
            subsets(idx+1, sub)
            
            # dont take
            sub.pop()
            subsets(idx+1, sub)

        subsets(0, [])
        return res