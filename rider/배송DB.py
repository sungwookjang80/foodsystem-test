from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from 배송 import 배송

class 배송DB():
    def __init__(self):
        self.engine = create_engine('sqlite:///배송_table.db', echo=True, connect_args={'check_same_thread': False})

        배송.__table__.create(bind=self.engine, checkfirst=True)

    def list(self):
        DBsession = sessionmaker(bind=self.engine)
        session = DBsession()
        
        query = session.query(배송).all()
        return query
    
    def save(self, entity):
        DBsession = sessionmaker(bind=self.engine, expire_on_commit=False)
        session = DBsession()
        
        session.add(entity)
        session.commit()
    
    def find_by_id(self, id:int):
        DBsession = sessionmaker(bind=self.engine)
        session = DBsession()
        try:
            query = session.query(배송).filter_by(id=id).one()
        except Exception as err:
            print(type(err))
            return err
        else:
            return query
            
    def update(self, id, request):
        DBsession = sessionmaker(bind=self.engine)
        session = DBsession()
        
        try:
            query = session.query(배송).filter(배송.id==id).first()
            query_dict = query.__dict__
            for key, value in request.items():
                if key in query_dict:
                    if key != 'id' and key != '_sa_instance_state':
                        setattr(query, key, value)
                
        except Exception as err:
            print(err)
            return err
        else:
            session.commit()
            return query
            
    def delete(self, id):
        DBsession = sessionmaker(bind=self.engine)
        session = DBsession()
        
        try:
            query = session.query(배송).filter_by(id=id).one()
            session.delete(query)
        except Exception as err:
            print('error:',err)
            return err
        else:
            session.commit()
            return None

repository = 배송DB()