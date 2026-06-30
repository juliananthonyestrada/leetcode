from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        heapq.heapify(hand)

        while freq:
            curr_size = 1
            smallest = heapq.heappop(hand)

            # heap may lag behind freq — skip already-exhausted cards
            if smallest not in freq:
                continue

            freq[smallest] -= 1
            if not freq[smallest]:
                del freq[smallest]

            while curr_size < groupSize:
                if smallest + 1 in freq:
                    curr_size += 1
                    freq[smallest + 1] -= 1
                    if not freq[smallest + 1]:
                        del freq[smallest + 1]
                    smallest += 1
                else:
                    return False

        return True