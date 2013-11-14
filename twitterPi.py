import twitter, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

api = twitter.Api(consumer_key='consumer_key', consumer_secret='consumer_secret', access_token_key='access_token', access_token_secret='access_token_secret')

lastTweetId = 0;

while True:
  statuses = api.GetUserTimeline(since_id=lastTweetId)
  for status in statuses:
    if int(status.id) > int(lastTweetId):
      lastTweetId = status.id

      GPIO.output(7,True)
      time.sleep(.5)
      GPIO.output(7,False)
      time.sleep(.5)

  time.sleep(60) #https://dev.twitter.com/docs/rate-limiting/1.1/limits
