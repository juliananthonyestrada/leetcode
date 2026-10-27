import heapq
from collections import defaultdict
from typing import List


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # cuisine -> heap of (-rating, food); may contain stale entries
        self.cuisine_heaps = defaultdict(list)

        # food -> (-rating, cuisine); source of truth for current ratings
        self.food_info = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (-rating, cuisine)
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        _, cuisine = self.food_info[food]
        self.food_info[food] = (-newRating, cuisine)

        # Old entry stays in the heap and is removed lazily in highestRated
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]

        # Pop stale entries whose rating no longer matches the current one
        while heap[0][0] != self.food_info[heap[0][1]][0]:
            heapq.heappop(heap)

        return heap[0][1]