from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import datetime

engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    shows = relationship("Shows", back_populates ="channel")
    created_at = Column(DateTime)
    
    def __repr__(self):
        return self.name


class Shows(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey("channels.id"))
    start_datetime = Column(DateTime(), nullable=False)
    rate = Column(Integer)
    name = Column(String(length=40), nullable=False)
    channel = relationship("Channel", back_populates="shows")

    def __repr__(self):
        return "<Name='%s', start_datetime='%s', rate='%s', channel='%s'>\n" % \
            (self.name, self.start_datetime, self.rate, self.channel)

Base.metadata.create_all(engine)

nickelodeon = Channel(name="Nickelodeon", created_at=datetime.datetime.now())
nickelodeon.shows = [
    Shows(rate="7", start_datetime=datetime.date(2007, 9, 8), name="iCarly"),
    Shows(rate="7", start_datetime=datetime.date(2010, 3, 27), name="Victorious"),
    
]

mtv = Channel(name="MTV", created_at=datetime.datetime.now())
mtv.shows = [
    Shows(name="Counting Stars", rate="7", start_datetime=datetime.date(1999, 8, 13)),
    Shows(name="Pimp My Ride", rate="6", start_datetime=datetime.date(2004, 3, 4)),
    Shows(name="Trick My Truck", rate="6", start_datetime=datetime.date(2006, 4, 25))
]

session.add(nickelodeon)
session.add(mtv)
session.commit

nickelodeon = session.query(Channel).filter_by(name="Nickelodeon").one()
mtv = session.query(Channel).filter_by(name="MTV").one()
print(nickelodeon.shows)
print(mtv.shows)


