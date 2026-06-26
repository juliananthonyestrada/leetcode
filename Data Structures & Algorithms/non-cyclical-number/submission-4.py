class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while True:
            n = str(n)
            running_sum = 0

            for s in n:
                running_sum += int(s)*int(s)

            n = running_sum

            if running_sum == 1:
                return True
            if running_sum in seen:
                return False

            seen.add(running_sum)
