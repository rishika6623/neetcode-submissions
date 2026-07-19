class Twitter:

    def __init__(self):
        self.global_timer = 0 
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.global_timer, tweetId))
        self.global_timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        new_feed = self.posts[userId].copy()
        heapq.heapify(new_feed)
        for following in self.following[userId]:
            for post in self.posts[following]:
                heapq.heappush(new_feed, post)
        i = 0
        news = []
        print(new_feed)
        while new_feed and i<10:
            i+=1
            news.append(heapq.heappop(new_feed)[1])
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
