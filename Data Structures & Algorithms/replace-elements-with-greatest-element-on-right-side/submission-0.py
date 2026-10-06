class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_seen = -1
        ptr = len(arr)-1

        while ptr > -1:
            temp = arr[ptr]
            arr[ptr] = max_seen
            max_seen = max(max_seen, temp)
            ptr -= 1
        
        return arr