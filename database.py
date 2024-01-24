# database.py
from sqlalchemy import Column, Integer, DateTime, create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./log.db"

engine = create_engine(DATABASE_URL)
conn = engine.connect()


Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    request = Column(String(255))
   
    response = Column(String(255))
    turnaround_time = Column(Integer)


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
