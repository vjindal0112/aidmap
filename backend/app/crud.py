from sqlalchemy.orm import Session

from __init__ import Tweet, Event
from schemas import EventCreate, TweetCreate


def get_tweet(db: Session, tweet_id: int):
    return db.query(Tweet).filter(Tweet.id == tweet_id).first()


def get_tweets_unprocessed(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tweet).limit(limit).all()


def create_event(db: Session, event: EventCreate):
    db_event = Event(lat=event.lat, long=event.long, event_type=event.event_type)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def create_tweet(db: Session, tweet: TweetCreate):
    db_tweet = Tweet(text=tweet.text, is_processed=tweet.is_processed)
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).limit(limit).all()
