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
            if r[0] < d[0]:
                d.popleft()
                r.append(r[0] + n)
                r.popleft()
            else:
                r.popleft()
                d.append(d[0] + n)
                d.popleft()
        
        return "Dire" if d else "Radiant"