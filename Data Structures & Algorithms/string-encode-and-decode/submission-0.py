class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        
        for word in strs:
            encoded_str += str(len(word))   # add length
            encoded_str += "*"              # add a divider
            encoded_str += word             # add the actual word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        
        decoded_list = []
        curr_len = curr_word = ""
        i = 0
        
        while i < len(s):                   # traverse entire decoded string
            if s[i] == "*":                 # we have captured the length
                ctr = 0                     # reset counter
                i += 1                      # start at first letter
                while ctr < int(curr_len):  # add all chars in the word
                    curr_word += s[i]
                    i += 1
                    ctr += 1
                
                decoded_list.append(curr_word)
                curr_len = curr_word = ""
            else:                           # we have not reached divider, add int
                curr_len += s[i]
                i += 1
                
        return decoded_list