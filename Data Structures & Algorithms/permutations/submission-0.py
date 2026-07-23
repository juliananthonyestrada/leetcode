class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []

        def perm(arr):

            if len(arr) == len(nums):
                permutations.append(arr.copy())

            for n in nums:
                if n in arr:
                    continue
                else:
                    arr.append(n)
                    perm(arr)
                    arr.pop()

        perm([])    
        
        return permutations