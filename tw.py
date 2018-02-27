import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "2YpVO5BVP3SmAZkHM4W2qI6iQ",
    "consumer_secret"     : "vl1BQyfhDZWQ5McNELnWjBP500myOitYM1SBigBT61otqn3Wi4",
    "access_token"        : "968400166972731392-vWEpJiCKWRiVhN2sumPId3YeVEQhxJq",
    "access_token_secret" : "yTw7OfhmUsfXQi2BILT3BEbRdFiPrYOfuNX2x8lr7c8lm" 
    }
  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing
if __name__ == "__main__":
  main()
