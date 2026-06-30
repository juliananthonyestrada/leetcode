class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # build our freq_map
        freq = {}

        for card in hand:
            if card in freq:
                freq[card] += 1
            else:
                freq[card] = 1

        def find_smallest():
            smallest = float('inf')

            for card in freq.keys():
                smallest = min(card, smallest)
            
            return smallest

        while freq:
            curr_size = 1
            smallest = find_smallest()
            freq[smallest] -= 1
            if not freq[smallest]:
                del freq[smallest]
            while curr_size < groupSize:
                if smallest+1 in freq.keys():
                    curr_size += 1
                    freq[smallest+1] -= 1
                    if freq[smallest+1] == 0:
                        del freq[smallest+1]
                    smallest += 1
                else:
                    return False
        return True