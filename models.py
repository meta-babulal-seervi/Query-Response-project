from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class QueryResponse(Base):
    __tablename__ = "query_responses"

    id = Column(Integer, primary_key=True, index=True)
    queries = Column(String, nullable=False)
    response = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())

    