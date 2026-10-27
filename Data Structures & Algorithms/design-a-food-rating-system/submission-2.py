from collections import defaultdict
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # cuisine -> heap[(rating, food)]
        self.heaps = defaultdict(list)

        # food -> (rating, cuisine)
        self.foods = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.foods[f] = (-r, c)
            heapq.heappush(self.heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        _, cuisine = self.foods[food]
        self.foods[food] = (-newRating, cuisine)

        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # curr highest rating does not match most updated rating
        while self.heaps[cuisine][0][0] != self.foods[self.heaps[cuisine][0][1]][0]:
            heapq.heappop(self.heaps[cuisine])
        
        return self.heaps[cuisine][0][1]