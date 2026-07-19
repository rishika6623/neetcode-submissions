class Twitter:

    def __init__(self):
        self.global_timer = 0 
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.global_timer, tweetId))
        self.global_timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        new_feed = []
        heapq.heapify(new_feed)
        self.following[userId].add(userId)
        #timer, user, user_ptr, post
        for following in self.following[userId]:
            if len(self.posts[following])>0:
                user_ptr = len(self.posts[following]) - 1
                timer, post = self.posts[following][user_ptr]
                heapq.heappush(new_feed, (timer, following, user_ptr-1, post))
        i = 0
        news = []
        print(new_feed)
        while new_feed and i<10:
            i+=1
            timer, user, user_ptr, post = heapq.heappop(new_feed)
            news.append(post)
            if user_ptr >= 0:
                timer, post = self.posts[user][user_ptr]
                heapq.heappush(new_feed, (timer, user, user_ptr - 1, post))
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
