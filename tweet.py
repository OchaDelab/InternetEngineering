import tweepy

# APIキーとトークンの設定
consumer_key = 'EaMB5BW19VMQjwkeybH0S7fux'
consumer_secret = 'w4XhG1XJ2kVQXKP2Jf8nfT2ghDjqCobIcd5Ikhq98Mqc11Blit'
access_token = '137940050-k44NsV9445h7ySZhZXDs8aVxXSYtVlpS8YtdkFdd'
access_token_secret = '4cDHjDqCMASIdkIF9CXO296i23AKxMPkEob98kIMpd5di'
bearer_token='AAAAAAAAAAAAAAAAAAAAAJ%2BLxQEAAAAAtiSvhN6%2F3i3YGokjUDywWWzTmWM%3D2udZtBuPWlvFh9pXBzAp8iKCzgj27vMKYpgJtlwP4SXPLKTTPc'
# 認証とAPIオブジェクトの作成
#auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
#api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token)
# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

client.create_tweet(text="Hello")
# 特定のキーワードに関するツイートを取得
#tweets = api.user_timeline(count=2)
#for tweet in tweets:
#    print(tweet.text, '\n')
