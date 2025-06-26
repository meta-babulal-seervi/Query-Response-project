from fastapi import Depends, FastAPI, HTTPException, Query 
import   models , schemas
from database import  engine , SessionLocal
from sqlalchemy.orm import Session 
import llm
models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally :
        db.close()

@app.post("/quries/" , response_model=schemas.QueryResponseOut)
def create_new_query(data : schemas.InputQuery , db:Session = Depends(get_db)) :
    response_data= llm.getResponse(data.prompt)
    new_query_response = models.QueryResponse(queries = data.prompt , response = response_data ) 
    db.add(new_query_response)
    db.commit()
    db.refresh(new_query_response)
    return new_query_response

# @app.get("/queries/" , response_model=list[schemas.QueryResponseOut])
# def get_all_queries(db:Session = Depends(get_db)) :
#     return db.query(models.QueryResponse).all()

@app.get("/queries/page/{page}", response_model=list[schemas.QueryResponseOut])
def get_queries_by_page(
    page: int,
    db: Session = Depends(get_db),
    page_size: int = 10  # Fixed page size, or make this a query param if you want it flexible
):
    if page < 1:
        raise HTTPException(status_code=400, detail="Page number must be >= 1")

    skip = (page - 1) * page_size
    return db.query(models.QueryResponse).offset(skip).limit(page_size).all()


