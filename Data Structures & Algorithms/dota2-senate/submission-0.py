class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        def next_enemy(current, enemy_char):
            for offset in range(1, n + 1):
                i = (current + offset) % n
                if senate[i] == enemy_char and not eliminated[i]:
                    return i
        
        s, n = 0, len(senate)
        eliminated = [False] * n
        Rs, Ds = senate.count("R"), senate.count("D")

        while True:
            # winner
            if Rs == 0:
                return "Dire"
            elif Ds == 0:
                return "Radiant"

            # continue eliminating
            if senate[s%n] == "R" and not eliminated[s%n]:
                i = next_enemy(s%n, "D")
                eliminated[i] = True
                Ds -= 1
            elif senate[s%n] == "D" and not eliminated[s%n]:
                i = next_enemy(s%n, "R")
                eliminated[i] = True
                Rs -= 1
            
            s += 1


        