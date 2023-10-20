import util
import 주문DB
from 주문 import 주문
주문repository = 주문DB.repository

import 결재DB
from 결재 import 결재
결재repository = 결재DB.repository


from 취소함 import 취소함

def whenever취소함_취소결재(data):
    event = 취소함()
    event = util.AutoBinding(data, event)
    
    주문 = 주문()
    주문repository.save(주문)
    결재 = 결재()
    결재repository.save(결재)
    
from 앱에등록 import 앱에등록

def whenever앱에등록_배송알림(data):
    event = 앱에등록()
    event = util.AutoBinding(data, event)
    
    주문 = 주문()
    주문repository.save(주문)
    결재 = 결재()
    결재repository.save(결재)
    

