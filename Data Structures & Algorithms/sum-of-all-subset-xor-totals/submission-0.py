class Solution:

    def xor_total(self, nums: List[int]) -> int:
        if not nums:
            return 0

        running = nums[0]

        for num in nums[1:]:
            running ^= num
        
        return running

    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0

        def subsets(idx, sub):
            nonlocal res

            if idx == len(nums):
                res += self.xor_total(sub)
                return
            
            sub.append(nums[idx])
            subsets(idx+1, sub)

            sub.pop()
            subsets(idx+1, sub)

        subsets(0, [])
        return res