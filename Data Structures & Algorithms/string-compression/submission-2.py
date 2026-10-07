class Solution:
    def compress(self, chars: List[str]) -> int:
        
        # iterate over the array with 2 pointers - 1 fixed at the start of the group and 1 that explores to see how far the group extends
        # l represents the beginning of the current group
        # r represents the end of the current group or beginning of the next group
        # k represents the next write position

        l, r, k = 0, 0, 0

        while r < len(chars):
            curr_ch = chars[l]
            # expand until we leave the group
            while r < len(chars) and chars[r] == curr_ch:
                r += 1
            
            group_size = (r-l)

            # write curr char at current write position
            chars[k] = curr_ch
            k += 1

            if group_size > 1:
                # modify input array to be char, freq
                digits = str(group_size)
                for digit in digits:
                    chars[k] = digit
                    k += 1            
            # move to next group
            l = r

        return k
