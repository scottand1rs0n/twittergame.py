
import tweepy, time, sys, random
from random import randint

argfile = str("liners.txt")



#enter the corresponding information from your Twitter application:
CONSUMER_KEY =  'Y4MNf0Vu6OGNOpO6TslG03ZkU'
CONSUMER_SECRET = 'ZcTwRLjPGhaahIvEpoGRvcVH4PTng3DbY4MIhqIlmtzse1tYNs'
ACCESS_KEY = '889493055782387712-9jGNpXKTwvDQSXIPP3pJLKX6T7c46J6'
ACCESS_SECRET = '9k1wjJSQ8AbFvyQ7007iqVOMuwYyIeW5Aasfeyjx6q5i0'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

while True:
    for line in f:
        curtime= time.strftime("%H:%M:%S")
        curdate= time.strftime("%x")
        api.update_status("{0}---{1}, {2}".format(curdate,curtime,line))
        TimeToSleep = randint(780,1200)
        time.sleep(TimeToSleep)#Tweet every 15 minutes
