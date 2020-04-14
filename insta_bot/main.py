import os
from insta_bot import InstaBot
from insta_db  import InstaDB

insta_user = 'rajanpupa'
insta_pass = os.getenv('INSTA_PASSWORD')

##  browser
my_bot = InstaBot( insta_user, insta_pass );
my_bot.navigate_profile_page(insta_user)
followers = my_bot.find_followers()
followees = my_bot.find_followers()
# followers = ['redsky_nrg']
# followees = ['redsky_nrg']

all_users = set(followers).union(set(followees))


print("followers=", followers)
print("followees=", followers)

## database
db = InstaDB()

userid = db.insert_user(insta_user)
# userid=1
user = db.get_user(insta_user);

for username in all_users:
    db.insert_user(username)
for username in followers:
    follower = db.get_user(username);
    db.save_follows(follower, user)
for username in followees:
    followee = db.get_user(username);
    db.save_follows(user, followee)

print("Data saved Successfully");
