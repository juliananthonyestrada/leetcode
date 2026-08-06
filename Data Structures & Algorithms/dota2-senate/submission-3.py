class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r = deque()
        d = deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            r_curr = r.popleft()
            d_curr = d.popleft()

            if r_curr < d_curr:
                r.append(r_curr+ n)
            else:
                d.append(d_curr + n)
        
        return "Dire" if d else "Radiant"