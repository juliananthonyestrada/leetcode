class Twitter:

    def __init__(self):
        self.following = defaultdict(set)   # person : set of who they are following
        self.posts = defaultdict(list)      # person : stack of their posts (cap at size 10)
        self.ctr = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.ctr, tweetId))
        self.ctr += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        people = self.following[userId] | {userId}
        res, heap = [], []
        added = 0

        for person in people:
            if self.posts[person]:
                ctr, tweetId = self.posts[person][-1]
                idx = len(self.posts[person])-1
                heapq.heappush(heap, (ctr, tweetId, person, idx))
        
        while heap and len(res) < 10:
            ctr, tweetId, person, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx-1 >= 0:
                new_ctr, new_tweetId = self.posts[person][idx-1]
                heapq.heappush(heap, (new_ctr, new_tweetId, person, idx-1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
