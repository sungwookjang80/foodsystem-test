from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Integer, event, Float, Boolean
from datetime import datetime

import util
from 결재됨 import 결재됨
from 취소됨 import 취소됨

Base = declarative_base()

class 결재(Base):
    __tablename__ = '결재_table'
    id = Column(Integer, primary_key=True)

    def __init__(self):
        self.id = None

@event.listens_for(결재, 'after_insert')
def PostPersist(mapper, connection, target):
    event = 결재됨()
    event = util.AutoBinding(target, event)

    event.Publish()
    
    event = 취소됨()
    event = util.AutoBinding(target, event)

    event.Publish()
    

    

