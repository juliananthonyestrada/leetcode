class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_subarray(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            return arr

        # reverse entire array
        nums.reverse()

        # take remainder
        length = len(nums)
        r = k % length

        reverse_subarray(nums, 0, r-1)
        reverse_subarray(nums, r, length-1)     
