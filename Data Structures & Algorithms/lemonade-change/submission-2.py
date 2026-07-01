class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # trap: considering total cash value instead of discrete bills

        # we start with no money on hand
        # if the first bill is anything but a 5

        # we cant give back any change 
        if bills[0] > 5:
            return False
        
        # track our money in a hash map -> bill_value : count
        register = {
            5 : 0,
            10 : 0,
            20 : 0
        }

        for bill in bills:
            register[bill] += 1

            # we need to return 
            change = bill - 5

            # give back biggest bills first and work backwards
            while change >= 20:
                if register[20]:
                    change -= 20
                    register[20] -= 1
                else:
                    break
            
            while change >= 10:
                if register[10]:
                    change -= 10
                    register[10] -= 1
                else:
                    break
            
            while change >= 5:
                if register[5]:
                    change -= 5
                    register[5] -= 1
                else:
                    break

            if change > 0:
                return False
            
        return True
            
