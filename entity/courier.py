from sqlalchemy import Column, Integer, String, DECIMAL, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Courier(Base):
    __tablename__ = 'courier'

    courier_id = Column(Integer, primary_key=True)
    sender_name = Column(String(255), nullable=False)
    sender_address = Column(String(255), nullable=False)
    receiver_name = Column(String(255), nullable=False)
    receiver_address = Column(String(255), nullable=False)
    weight = Column(DECIMAL(5, 2), nullable=False)
    status = Column(String(50), nullable=False)
    tracking_number = Column(String(20), unique=True, nullable=False)
    delivery_date = Column(Date, nullable=False)
