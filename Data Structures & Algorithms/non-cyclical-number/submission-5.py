class Solution:
    def isHappy(self, n: int) -> bool:
        
        def convert(n: int) -> int:
            n = str(n)
            running_sum = 0

            for s in n:
                running_sum += int(s)*int(s)

            return running_sum


        seen = set()

        while True:
            n = convert(n)

            if n == 1:
                return True
            elif n in seen:
                return False

            seen.add(n)
