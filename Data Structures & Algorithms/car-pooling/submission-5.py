class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # line sweep
        curr_size = 0
        points = []

        for passengers, pickup, dropoff in trips:
            points.append([pickup, passengers])
            points.append([dropoff, -passengers])
        
        points.sort()

        for point, passenger in points:
            curr_size += passenger
            if curr_size > capacity:
                return False
        
        return True
