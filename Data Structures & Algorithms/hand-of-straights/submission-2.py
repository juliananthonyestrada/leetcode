class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # build our freq_map
        freq = {}
        for card in hand:
            if card in freq:
                freq[card] += 1
            else:
                freq[card] = 1

        # helper function to find the start of the next hand
        def find_smallest():
            smallest = float('inf')
            for card in freq.keys():
                smallest = min(card, smallest)
            return smallest

        # while we have cards to shuffle
        while freq:
            # begin with the current group
            curr_size = 1
            # find the start
            smallest = find_smallest()
            # decrement its freq and delete if needed
            freq[smallest] -= 1
            if not freq[smallest]:
                del freq[smallest]
            # continue searching for cards until we meet the group size
            while curr_size < groupSize:
                # if our card exists
                if smallest+1 in freq.keys():
                    # increment group size, decrement card freq, and delete if needed
                    curr_size += 1
                    freq[smallest+1] -= 1
                    if freq[smallest+1] == 0:
                        del freq[smallest+1]
                    smallest += 1
                # card does not exist, we fail
                else:
                    return False

        # no more cards to shuffle, all done
        return True