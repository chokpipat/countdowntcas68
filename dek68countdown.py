import tweepy
from datetime import datetime
import schedule
import time

api_key = "4y6sq8Pq0nrlmkKdB2wQ9MJku"
api_secret = "WPVsmbJThu0VBlzP5xeCt0pJwT0Y2DW1XjZPCP4wEtOa6bAr0W"
access_token = "1833344657339912193-a0dpEnhw0dF3kVjbgokjffQPL3RhwQ"
access_token_secret = "yGOXlSvpwH9BnUfphlmDHXFALx7tksgxRfKTK9Uus7GB2"

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

events = {
    "TGAT/TPAT2-5": datetime(2024, 12, 7),
    "TPAT1(กสพท)": datetime(2024, 12, 14),
    "A-Level": datetime(2025, 3, 8),
}

def tweet():
    current_date = datetime.now()
    tweets = []

    for event_name, target_date in events.items():
        days_left = (target_date - current_date).days
        tweets.append(f"เหลืออีก {days_left} วัน จนถึงสอบ {event_name} 68!")
    
    format_tweet = "\n".join(tweets) + "\n#dek68 #TCAS68"
    
    api.update_status(format_tweet)
    print("Tweeted successfully!")

schedule.every().day.at("09:00").do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
