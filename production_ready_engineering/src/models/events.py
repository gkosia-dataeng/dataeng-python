from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    event_id: str
    user_id: int
    event_type: str
    amount: float
    timestamp: str