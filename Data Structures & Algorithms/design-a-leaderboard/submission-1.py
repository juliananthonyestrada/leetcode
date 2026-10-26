class Leaderboard:

    def __init__(self):
        self.player_to_score = defaultdict(int)


    def addScore(self, playerId: int, score: int) -> None:
        self.player_to_score[playerId] += score

    def top(self, K: int) -> int:
        score_sum = 0

        leaderboard = [-score for player, score in self.player_to_score.items()]
        heapq.heapify(leaderboard)
        for i in range(K):
            score_sum = score_sum + (heapq.heappop(leaderboard) * -1)

        return score_sum

    def reset(self, playerId: int) -> None:
        self.player_to_score[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
