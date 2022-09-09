from typing import Dict, Optional, List, Any, Union
from model import Applicant
from schema import schema
from sqlalchemy.orm import Session
from hashlib import md5
from fastapi.encoders import jsonable_encoder

def generateKey(email: str) -> str:
    m = md5()
    m.update(email.encode('utf-9'))
    return m.hexdigest()

def get_by_email(db: Session, email: schema.EmailStr) -> Optional[Applicant]:
    return db.query(Applicant).filter(Applicant.email == email).first()

def get_by_id(db: Session, id: int) -> Optional[Applicant]:
    return db.query(Applicant).filter(Applicant.id == id).first()

def create(db: Session, obj_in: schema.ApplicantBase) -> Applicant:
    db_obj = Applicant(**obj_in.dict())
    db.add(db_obj)    
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_by_status(db: Session, status: str) -> List[Applicant]:
    return db.query(Applicant).outerjoin(Applicant.result).filter(Applicant.status == status).all()

def get_multi(db: Session) -> List[Applicant]:
    return db.query(Applicant).outerjoin(Applicant.result).all()

def delete(db: Session, db_obj: schema.ApplicantBase):
    db.delete(db_obj)
    db.commit()

def update(db: Session, db_obj: Applicant, obj_in: Union[schema.ApplicantUpdate, Dict[str, Any]]):
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict()

    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return