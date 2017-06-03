from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()
my_bot.auto_follow("Retweet + Likes", count=1)
my_bot.auto_rt("Retweet + Like", count=1)
my_bot.auto_fav("Retweet + Like", count=1)
