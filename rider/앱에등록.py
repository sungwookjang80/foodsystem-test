from AbstractEvent import AbstractEvent
import json
from datetime import datetime

class 앱에등록(AbstractEvent):
    id : int
    
    def __init__(self):
        super().__init__()
        self.id = None

