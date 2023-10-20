from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer, event, Float, Boolean
from datetime import datetime

import util
from 승인완료 import 승인완료
from 거절함 import 거절함
from 요리시작 import 요리시작
from 완료 import 완료

Base = declarative_base()

class 주문확인(Base):
    __tablename__ = '주문확인_table'
    id = Column(Integer, primary_key=True)

    def __init__(self):
        self.id = None

@event.listens_for(주문확인, 'after_insert')
def PostPersist(mapper, connection, target):
    event = 승인완료()
    event = util.AutoBinding(target, event)

    event.Publish()
    
    event = 거절함()
    event = util.AutoBinding(target, event)

    event.Publish()
    
    event = 요리시작()
    event = util.AutoBinding(target, event)

    event.Publish()
    
    event = 완료()
    event = util.AutoBinding(target, event)

    event.Publish()
    

    

