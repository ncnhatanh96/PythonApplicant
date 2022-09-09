from typing import Optional, List
from model.model import Applicant, ProcessResult
from sqlalchemy.orm import Session
from hashlib import md5

def generateKey(email: str) -> str:
    m = md5()
    m.update(email.encode('utf-8'))
    return m.hexdigest()


def create(db: Session, obj_in: Applicant) -> Optional[ProcessResult]:

    isFailed = int(obj_in.dob.day) % 2
    db_obj = ProcessResult(applicant_id = obj_in.id,
                           client_key =  generateKey(obj_in.email) if isFailed == 0 else "",
                           applicant_status = "processed" if isFailed == 0 else "failed")
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get(db: Session, id: int) -> Optional[ProcessResult]:
    return db.query(ProcessResult).filter(ProcessResult.applicant_id == id).first()
