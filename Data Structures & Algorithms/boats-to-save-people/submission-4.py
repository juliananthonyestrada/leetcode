class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        boats, left, right = 0, 0, len(people)-1

        while left <= right:
            # overweight pairing - send the heavier one
            if people[left] + people[right] > limit:
                boats += 1
                right -= 1
            # valid pairing - send them both 
            else:
                boats += 1
                right -= 1
                left += 1

        return boats