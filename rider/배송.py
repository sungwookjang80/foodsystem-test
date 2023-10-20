from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer, event, Float, Boolean
from datetime import datetime

import util
from 배송시작 import 배송시작
from 앱에등록 import 앱에등록
from 완료 import 완료

Base = declarative_base()

class 배송(Base):
    __tablename__ = '배송_table'
    id = Column(Integer, primary_key=True)

    def __init__(self):
        self.id = None

@event.listens_for(배송, 'after_insert')
def PostPersist(mapper, connection, target):
    event = 배송시작()
    event = util.AutoBinding(target, event)

    event.Publish()
    
    event = 앱에등록()
    event = util.AutoBinding(target, event)

    event.Publish()
    
    event = 완료()
    event = util.AutoBinding(target, event)

    event.Publish()
    

    

