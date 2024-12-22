from fastapi import APIRouter, HTTPException
from app.models import Book
from app.database import books, books_id_num

book_router = APIRouter()

@book_router.post("/")
def create_book(book: Book):
    global books_id_num
    book.id = books_id_num
    books[books_id_num] = book
    books_id_num += 1
    return 

@book_router.get("/")
def books_list():
    return list(books.values())

@book_router.get("/{book_id}")
def book_get(book_id: int):
    book = books.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not available")
    return book
    
@book_router.put("/{book_id}")
def book_update(book_id: int, updated_book: Book):
    book = books.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not available")
    updated_book.id = book_id
    books[book_id] = updated_book

@book_router.patch("{book_id}/unavailable")
def book_unavailable(book_id: int):
    book = books.get(book_id)
    if not book: 
        raise HTTPException(status_code=404, detail="Book not available")
    updated_book = book.copy(update={"is_available": False})
    books[book_id] = updated_book  
    return {"message": f"Book {book_id} marked as unavailable"}   


