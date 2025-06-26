from datetime import datetime
from pydantic import BaseModel

class InputQuery(BaseModel):
    prompt: str

class QueryResponseOut(BaseModel):
    id: int
    queries: str
    response: str
    created_at: datetime

    class Config:
        from_attributes = True  
