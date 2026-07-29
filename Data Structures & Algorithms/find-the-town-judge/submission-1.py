class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # build a graph where a connection from a -> b
        # means that a trusts b
        # after doing this then the person with no 
        # outgoing connections is the town judge and n-1 incoming connections

        connections = {}

        for i in range(1, n+1):
            connections[i] = [0, 0]  # incoming, outgoing
        
        for a, b in trust:
            connections[a][1] += 1
            connections[b][0] += 1
        
        for person in connections:
            if connections[person][0] == n-1 and connections[person][1] == 0:
                return person
        return -1
