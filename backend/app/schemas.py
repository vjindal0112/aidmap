from pydantic import BaseModel


class EventBase(BaseModel):
    event_type: str
    lat: float
    long: float


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int

    class Config:
        orm_mode = True


class TweetBase(BaseModel):
    text: str
    is_processed: bool


class TweetCreate(TweetBase):
    pass


class Tweet(TweetBase):
    id: int

    class Config:
        orm_mode = True
