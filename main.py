from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List 

from model import model
from schema import schema
from crud import crud_applicant, crud_result
from database import SessionLocal, engine

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/applicant", response_model=List[schema.ApplicantINDB])
async def get_applicant(
        *,
        db: Session = Depends(get_database_session)
) -> Any:
    return crud_applicant.get_multi(db=db)

@app.get("/applicant/{status}", response_model=List[schema.ApplicantINDB])
async def get_applicant(
        *,
        db: Session = Depends(get_database_session),
        status: str
) -> Any:
    return crud_applicant.get_by_status(db=db, status=status)

@app.post("/applicant", response_model=schema.ApplicantOut)
async def add_applicant(
        *, 
        db: Session = Depends(get_database_session),
        applicant_in: schema.ApplicantBase
) -> Any:
    applicant = crud_applicant.get_by_email(db=db, email=applicant_in.email)
    if applicant:
        raise HTTPException (
            status_code=400,
            detail="This applicant already exists in system.",
        )
    applicant = crud_applicant.create(db=db, obj_in=applicant_in)
    return applicant

@app.post("/process/{id}", response_model=schema.ProcessResult)
async def process_applicant(
        *, 
        db: Session = Depends(get_database_session),
        id: int
) -> Any:
    applicant = crud_applicant.get_by_id(db=db, id=id)
    if applicant is None:
        raise HTTPException (
            status_code=404,
            detail="applicant doesn't exists in system.",
        )
    elif applicant.status == "processed":
        return crud_result.get(db=db, id=id)

    crud_applicant.update(db=db, db_obj=applicant, obj_in={"status": "processed"})
    result = crud_result.create(db=db, obj_in=applicant)
    return result

@app.delete("/applicant/{id}")
async def delete_applicant(
        *,
        db: Session = Depends(get_database_session),
        id: int
):
    applicant = crud_applicant.get_by_id(db=db, id=id)
    if applicant:
        crud_applicant.delete(db=db, db_obj=applicant)
    else:
        raise HTTPException (
            status_code=404,
            detail="applicant doesn't exists in system.",
        )
    return

@app.put("/applicant/{id}")
async def update_applicant(
    *,
    db: Session = Depends(get_database_session),
    id: int,
    applicant_in: schema.ApplicantBase
) -> Any:
    applicant = crud_applicant.get_by_id(db=db, id=id)
    if applicant is None:
        raise HTTPException (
            status_code=404,
            detail="applicant doesn't exists in system.",
        )
    crud_applicant.update(db=db, db_obj=applicant, obj_in=applicant_in)
    return "Updated"