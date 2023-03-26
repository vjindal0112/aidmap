from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
import crud
import schemas
import processor
from __init__ import SessionLocal

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tweets/", response_model=schemas.Tweet)
def create_tweet(tweet: schemas.TweetCreate, db: Session = Depends(get_db)):
    return crud.create_tweet(db=db, tweet=tweet)


@app.get("/")
async def root(db: Session = Depends(get_db)):
    temp = crud.get_tweet(db, 1)
    return {"message": temp}


@app.get("/process/")
def process(db: Session = Depends(get_db)):
    tweets = crud.get_tweets_unprocessed(db)
    print(tweets)
    for tweet in tweets:
        if tweet.is_processed is False:
            print(processor.process_tweet(tweet))
    return {"message": "Processed"}


@app.get("/events/", response_model=List[schemas.Event])
def get_events(db: Session = Depends(get_db)):
    return crud.get_events(db=db)
