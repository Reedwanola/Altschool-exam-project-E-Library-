from fastapi import APIRouter, HTTPException
from app.models import BorrowRecord
from app.database import users, books, borrow_record, borrow_record_id_num
from datetime import date


borrow_router = APIRouter()
@borrow_router.post("/")
def borrow_book(user_id: int, book_id: int):
    global borrow_record_id_num
    user = users.get(user_id)
    book = books.get(book_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user["is_active"]:
        raise HTTPException(status_code=400, detail="User is inactive")
    if not book:
        raise HTTPException(status_code=404, detail="Book not found") 
    if not book["is_available"]:
        raise HTTPException(status_code=400, detail="Book not available")
    
    for record in borrow_record.values():
        if record.user_id == user_id and record.book_id == book_id and not record.return_date:
            raise HTTPException(status_code=400, detail="Book already borrowed")
    borrow_records = BorrowRecord(id = borrow_record_id_num, user_id= user_id, book_id=book_id, borrow_date = date.today())
    borrow_record[borrow_record_id_num] = borrow_records
    borrow_record_id_num += 1
    book.is_available = False
    books[book_id] = book
    return borrow_records

@borrow_router.post("{record_id}/return")
def return_book(record_id: int):
    record = borrow_record.get(record_id)
    if not record or record.return_date:
          raise HTTPException(status_code=400, detail="Invalid borrow record or book already returned")
    record.return_date = date.today()
    books[record.book_id].is_available

    return {"message": f"Record {record_id} marked as returned"}

       


