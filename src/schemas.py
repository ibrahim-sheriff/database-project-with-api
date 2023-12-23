from datetime import date

from pydantic import BaseModel


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone: str = None
    date_of_birth: date = None
    address: str = None
