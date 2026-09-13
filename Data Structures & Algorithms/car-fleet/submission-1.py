class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = [[pos, spd] for pos, spd in zip(position, speed)] 
        arr.sort()

        stack = []

        for pos, spd in reversed(arr):
            time = (target - pos) / spd
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)