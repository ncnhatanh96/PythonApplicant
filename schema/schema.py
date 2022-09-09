from typing import Optional
from pydantic import BaseModel, EmailStr
import datetime
from model import CountryEnum

class ApplicantBase(BaseModel):
    name: str
    email: EmailStr
    dob: datetime.date
    country: CountryEnum

class ApplicantOut(BaseModel):
    id: int
    status: str
    class Config:
        orm_mode = True

class ApplicantUpdate(ApplicantBase):
    status: str = None


class ApplicantResult(BaseModel):
    client_key: str
    applicant_status: str
    processed_dttm: datetime.datetime

    class Config:
        orm_mode = True

class ApplicantINDB(ApplicantBase):
    id: int
    status: str
    result: Optional[ApplicantResult]
    class Config:
        orm_mode = True

class ProcessResult(ApplicantResult):
    applicant_id: int
