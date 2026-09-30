class Twitter:

    def __init__(self):
        self.following = {} # user Id: set(following)
        self.count = 0
        self.tweet = {} # userId: [(count, tweetId)] array

        '''
        self.tweet = 
        {
            1: [(0, 10)]
            2: [(1, 20)]
        }
        '''


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet:
            self.tweet[userId] = []
        self.tweet[userId].append((self.count, tweetId)) # {userId: [(count, tweetId)]}
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]: # Return tweetid
        self.intFeed = [] # min heap (to pop the small ones)

        # users own tweet
        if userId in self.tweet:
            for count, tweetId in self.tweet[userId]:
                heapq.heappush(self.intFeed, (count, tweetId))
                if len(self.intFeed) > 10:
                    heapq.heappop(self.intFeed) # pop the smallest counts

    
        if userId in self.following:
            for followingId in self.following[userId]:
                followingTweet = self.tweet[followingId]
                for count, tweetId in followingTweet:
                    heapq.heappush(self.intFeed, (count, tweetId))
                    if len(self.intFeed) > 10:
                        heapq.heappop(self.intFeed)

        ans = []
        while len(self.intFeed) > 0:
            count, tweetId = heapq.heappop(self.intFeed)
            ans.append(tweetId)
        ans.reverse()
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        
