class Twitter:

    def __init__(self):
        self.tweetId = 0
        self.followers = []
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetId += 1
        self.tweets.append([userId, -tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        
        k = 10
        user_followers = [userId]
        
        # get followers
        for item in self.followers:
            if item[0] == userId:
                user_followers.append(item[1])
        
        temp = self.tweets
        
        heapq.heapify(temp)
        
        result = []
        
        if len(temp) > k:
            while len(temp) > k and k > 0:
                item = heapq.heappop(temp)
                if item[0] in user_followers:
                    result.append(abs(item[1]))
                    k -= 1
        else:
            while len(temp) > 0:
                item = heapq.heappop(temp)
                if item[0] in user_followers:
                    result.append(abs(item[1]))
                    k -= 1
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers.append([followerId, followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if [followerId, followeeId] in self.followers:
            self.followers.remove([followerId, followeeId])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)