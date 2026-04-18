class Twitter:

    def __init__(self):
        self.tweet = {}
        self.follower = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet:
            self.tweet[userId].append((self.time, tweetId))
        else:
            self.tweet[userId] = [(self.time, tweetId)]
        
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId]
        users.extend(self.follower.get(userId, []))

        heap = []
        for u in users:
            if u in self.tweet:
                idx = len(self.tweet[u]) - 1
                t, val = self.tweet[u][idx]
                heapq.heappush(heap, (t, val, u, idx - 1))
        
        result = []
        while heap and len(result) < 10:
            _, val_curr, u, idx = heapq.heappop(heap)
            if val_curr not in result:
                result.append(val_curr)
            
            if idx >= 0:
                t, val = self.tweet[u][idx]
                heapq.heappush(heap, (t, val, u, idx - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower:
            self.follower[followerId].add(followeeId)
        else:
            self.follower[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followed = self.follower.get(followerId)
        if followed and followeeId in followed:
            followed.remove(followeeId)
