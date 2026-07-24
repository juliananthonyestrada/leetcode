class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []                    
        used = [False] * len(nums)

        def perm(arr):
            if len(arr) == len(nums):
                permutations.append(arr.copy())
                return

            for i, n in enumerate(nums):
                if used[i]:
                    continue
                else:
                    used[i] = True
                    arr.append(n)
                    perm(arr)
                    arr.pop()
                    used[i] = False

        perm([])    
        
        return permutations