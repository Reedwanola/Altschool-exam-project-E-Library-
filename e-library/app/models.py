from pydantic import BaseModel
from typing import Optional
from datetime import date

class User(BaseModel):
    name: str
    email: str
    id: Optional[int]
    is_active: bool = True 
    
class Book(BaseModel):
    title: str
    author: str
    id: Optional[int]
    is_available: bool = True

class BorrowRecord(BaseModel):
    id: Optional[int]
    user_id: int
    book_id: int
    borrow_date: date
    return_date: date



