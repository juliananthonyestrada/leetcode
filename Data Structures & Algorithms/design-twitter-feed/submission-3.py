class Twitter:
    from collections import heapq, defaultdict

    def __init__(self):
        self.users = defaultdict(set)   # user : (followers)
        self.posts = []                 # heap (ctr, tweetId, userId)
        self.ctr = 1
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, (-self.ctr, tweetId, userId))
        self.ctr += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        added, res = 0, []
        removed = []

        while self.posts:
            ctr, tweet, poster = heapq.heappop(self.posts)
            removed.append((ctr, tweet, poster))
            
            # post is made by me or someone i follow
            if poster == userId or poster in self.users[userId]:
                res.append(tweet)
                added += 1

            if added == 10:
                for r in removed:
                    heapq.heappush(self.posts, r)
                return res
        
        for r in removed:
            heapq.heappush(self.posts, r)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
