class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # trap: considering total cash value instead of discrete bills

        # if the first bill is anything but a 5
        # we cant give back any change 
        if bills[0] > 5:
            return False
        
        # most ever paid is 20 -> we only ever have to return 5s or 10s
        fives, tens = 0, 0

        for bill in bills:
            # no change
            if bill == 5:
                fives += 1
            # return 5
            elif bill == 10:
                tens += 1
                if fives == 0:
                    return False
                else:
                    fives -= 1
            # return 15
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True
            