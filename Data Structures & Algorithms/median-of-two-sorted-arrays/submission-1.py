class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # A holds the smaller array
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)-1
        total = len(A)+len(B)
        need = total//2

        while True:
            # take partitions from each array
            i = (r + l) // 2
            j = need-i-2

            # do these create the entire left partition ?

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
                l = i + 1
            else:
                if total % 2:
                    return min(Aright, Bright) / 1
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
