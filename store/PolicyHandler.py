import util
import 주문확인DB
from 주문확인 import 주문확인
주문확인repository = 주문확인DB.repository


from 결재됨 import 결재됨

def whenever결재됨_주문접수(data):
    event = 결재됨()
    event = util.AutoBinding(data, event)
    
    주문확인 = 주문확인()
    주문확인repository.save(주문확인)
    
from 취소됨 import 취소됨

def whenever취소됨_취소알림(data):
    event = 취소됨()
    event = util.AutoBinding(data, event)
    
    주문확인 = 주문확인()
    주문확인repository.save(주문확인)
    
from 배송확인 import 배송확인

def whenever배송확인_배송확인완료(data):
    event = 배송확인()
    event = util.AutoBinding(data, event)
    
    주문확인 = 주문확인()
    주문확인repository.save(주문확인)
    

