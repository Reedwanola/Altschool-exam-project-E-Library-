from fastapi import FastAPI
from app.routes.users import user_router
from app.routes.books import book_router
from app.routes.borrows import borrow_router

app = FastAPI(title="E-Library API System")

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrow_router, prefix="/borrow", tags=["Borrow Records"])



app.get("/")
def home():
    return {"Message":"Welcome to the E-library"}


