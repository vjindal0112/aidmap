from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
import crud
import schemas
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
