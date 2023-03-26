from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, Integer, String, Float, Time


SQLALCHEMY_DATABASE_URL = "postgresql://varun:@localhost:5432/main"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)


class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    is_processed = Column(Boolean, default=False)


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    long = Column(Float)
    event_type = Column(String)
    time = Column(Time)