class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        verification_list = set()
        flag = False
        for i in nums:
           if i in verification_list:
               flag = True
               return flag
           verification_list.add(i)
        flag = False
        return flag
    