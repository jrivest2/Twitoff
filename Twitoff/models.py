"""SQLAlchemy models and utility functions for Twitoff Application"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter User Table that will correspond to tweets = SQLAlchemy syntax"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    name = DB.Column(DB.String, nullable=False) # name column
    newest_tweet_id = DB.Column(DB.BigInteger) # Keeps track of recent tweet
    # num_tweets = DB.Column(DB.BigInteger, nullable=True)
    # total_likes = DB.Column(DB.BigInteger, nullable=True)
    def __init__(self,id,name):
        self.id = id
        self.name = name
        # self.total_likes = self.count_likes()
        # self.num_tweets = len(self.tweets)

    def count_likes(self):
        count = 0
        for tweet in self.tweets:
            count += tweet.likes
        return count
    
    # def __repr__(self):
    #     return "<User: {}'>\n<Likes: {}>'\n<Tweets: {}>".format(self.name,self.total_likes,self.num_tweets)

class Tweet(DB.Model):
    """Tweet text data - associated with Users Table"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    text = DB.Column(DB.Unicode(250)) # Tweet text column
    vect = DB.Column(DB.PickleType, nullable=False) # 
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=True)
    user= DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    # likes = DB.Column(DB.BigInteger, nullable=True)
    
    # def __init__(self,id,text,user,likes=0):
    #     # User.id.total_likes += likes
    #     self.id = id
    #     self.text = text
    #     self.user = user
    #     self.likes = likes
    #     self.user.total_likes += self.likes
    #     self.user.num_tweets += 1

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)
