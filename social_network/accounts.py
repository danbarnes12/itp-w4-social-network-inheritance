from social_network.posts import TextPost, PicturePost, CheckInPost

class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        
    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)

    def get_timeline(self):
        followed_posts = []
        for friends in self.following:
            for tweet in friends.posts:
                followed_posts.append(tweet)
        return sorted(followed_posts, key=lambda tweets: tweets.timestamp,reverse=True)

    def follow(self, other):
        self.following.append(other)
