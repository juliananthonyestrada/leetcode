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
        i = 0

        while i < len(s):                  
           j = s.index("*", i)                      # grab idx of *
           length = int(s[i:j])                     # grab length of curr word
           decoded_list.append(s[j+1:j+length+1])   # add word to list
           i = j+length+1                           # set marker for the next search

        return decoded_list