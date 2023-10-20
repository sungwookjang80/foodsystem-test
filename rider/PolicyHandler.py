import util
import 배송DB
from 배송 import 배송
배송repository = 배송DB.repository


from 배송확인 import 배송확인

def whenever배송확인_배송확인완료(data):
    event = 배송확인()
    event = util.AutoBinding(data, event)
    
    배송 = 배송()
    배송repository.save(배송)
    

