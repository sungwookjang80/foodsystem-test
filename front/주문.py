from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer, event, Float, Boolean
from datetime import datetime

import util
from 주문됨 import 주문됨
from 취소함 import 취소함

Base = declarative_base()

class 주문(Base):
    __tablename__ = '주문_table'
    id = Column(Integer, primary_key=True)

    def __init__(self):
        self.id = None

@event.listens_for(주문, 'after_insert')
def PostPersist(mapper, connection, target):
    event = 주문됨()
    event = util.AutoBinding(target, event)

    event.Publish()
    
    event = 취소함()
    event = util.AutoBinding(target, event)

    event.Publish()
    

    

