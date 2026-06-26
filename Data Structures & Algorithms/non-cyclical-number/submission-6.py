class Solution:
    def isHappy(self, n: int) -> bool:
        
        def convert(n: int) -> int:
            return sum(int(c) ** 2 for c in str(n))

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = convert(n)

        return n == 1