import tweepy

# APIキーとトークンの設定
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
bearer_token=''
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
