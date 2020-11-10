import sqlite3
import random
import string

conn = sqlite3.connect("db.sqlite3")
curs = conn.cursor()

NAMES= ['Justin', 'Jacob', 'Katie', 'Jen', 'Jon','Kira']
TWEETS = []

for i in range(10):
    x = random.sample(string.ascii_lowercase, k=10)
    TWEETS.append(''.join(x))

def add_user(users):
    for x in range(users):
        data = tuple([str(x), random.choice(NAMES)])
        curs.execute(f"INSERT INTO user (id, name) VALUES {tuple(data)}")

def add_tweets(tweets):
    for x in range(tweets):
        data = tuple([str(x), str(random.randint(0, 4)), random.choice(TWEETS)])
        curs.execute(f"INSERT INTO tweet (id, user_id, text) VALUES {tuple(data)}")


add_user(5)
add_tweets(7)

curs.close()
conn.commit()