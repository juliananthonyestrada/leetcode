class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = defaultdict(int)
        minimum = 0
        for i in range(len(hand)):
            freq[hand[i]] += 1
        
        while freq:
            minimum = min(freq)
            count = freq[minimum]
            for i in range(groupSize):
                if freq[minimum + i] - count < 0:
                    return False
                elif freq[minimum + i] - count == 0:
                    freq.pop(minimum + i)
                else:
                    freq[minimum + i] -= count
        return True