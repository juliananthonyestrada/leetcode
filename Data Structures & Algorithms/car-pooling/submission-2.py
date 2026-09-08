class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        size = 0
        heap = []   # (dropoff time, num passengers)
        trips.sort(key = lambda t : t[1] )

        for passengers, pickup, dropoff in trips:
            # drop off passengers 
            while heap and heap[0][0] <= pickup:
                size -= heapq.heappop(heap)[1] 

            heapq.heappush(heap, (dropoff, passengers)) 

            # pick up curr passengers 
            size += passengers
            if size > capacity:
                print(size, capacity)
                return False
        
        return True
