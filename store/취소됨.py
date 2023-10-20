
from AbstractEvent import AbstractEvent
import json

class 취소됨(AbstractEvent):
    id : int
    
    def __init__(self):
        super().__init__()
        self.id = None

