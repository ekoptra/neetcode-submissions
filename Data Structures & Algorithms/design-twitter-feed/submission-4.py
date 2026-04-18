class Twitter:

    def __init__(self):
        self.tweet = {}
        self.follower = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet:
            self.tweet[userId].append((self.time * -1, tweetId * -1))
        else:
            self.tweet[userId] = [(self.time * -1, tweetId * -1)]
        
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweet.get(userId, []))

        for f in self.follower.get(userId, []):
            feed += self.tweet.get(f, [])
        
        heapq.heapify(feed)
        result = []
        track = set()
        while (len(result) < 10) and feed:
            top_val = heapq.heappop(feed)[1] * -1
            if top_val not in track:
                result.append(top_val)
                track.add(top_val)
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower:
            self.follower[followerId].add(followeeId)
        else:
            self.follower[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followed = self.follower[followerId]
        if followeeId in followed:
            followed.remove(followeeId)
