class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 0:
            return []

        pfx = [0] * l
        pfx[0], pfx[1] = 1, nums[0]

        sfx = [0] * l
        sfx[-1], sfx[-2] = 1, nums[-1]

        ans = [0] * l

        for i in range(2,l):
            pfx[i] = pfx[i-1]*nums[i-1]

        for i in range(l-3, -1, -1):
            sfx[i] = nums[i+1]*sfx[i+1]
        
        for i in range(l):    
            ans[i] = pfx[i]*sfx[i]

        print(pfx)
        print(sfx)
        print(ans)

        return ans
