class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # go adding elements in order to a stack and like that we can check if there is a collision

        def direction(a: int):
            if a * -1 > 0:
                return "left"
            else:
                return "right"

        stack = []

        for a in asteroids:
            stack.append(a)

            # collision
            while len(stack) > 1 and direction(stack[-1]) == "left" and direction(stack[-2]) == "right":
                # case: equal values
                if abs(stack[-1]) == abs(stack[-2]):
                    stack.pop()
                    stack.pop()
                # case: bottom asteroid is smaller
                elif abs(stack[-1]) > abs(stack[-2]):
                    temp = stack.pop()
                    stack.pop()
                    stack.append(temp)
                # case: bottom asteroid is smaller
                else:
                    stack.pop()

        return stack