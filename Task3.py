from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    shows = relationship("Shows")
    created_at = Column(DateTime)
    
    def __repr__(self):
        return "<Channel(name='%s', created_at='%s', shows='%s')>" % \
    (self.name, self.created_at, self.shows)


class Shows(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey("channels.id"))
    start_datetime = Column(DateTime(), nullable=False)
    rate = Column(Integer)
    name = Column(String(length=40), nullable=False)
    channel = relationship("Channel")

    def __repr__(self):
        return "<Channel(name='%s', created_at='%s', shows='%s')>" % \
            (self.name, self.created_at, self.shows)

Base.metadata.create_all(engine)