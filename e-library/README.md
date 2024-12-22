E-Library API System
 A FastAPI-based project to manage users, books, and borrow/return operations in an E-Library.

Features
 Users: Create, update, and deactivate users.
 Books: Add, update, and mark books as unavailable.
 Borrows: Borrow and return books.
 In-Memory Storage: Data is stored temporarily for simplicity.

Setup Instructions
 Clone the Repository:
 git clone https://github.com/your-repo/e_library_api.git
 cd e_library_api

Set Up Virtual Environment:
 python -m venv e-library
 
To activate the virtual environment 
 e-library\Scripts\activate

Install FastAPI and all its dependencies
  On your terminal, type
  pip install fastapi[all]

Run the Server:
 On your terminal, type
 uvicorn main:app --reload

Access API Docs:
  Swagger UI: http://127.0.0.1:8000/docs

API Endpoints:
Users
 POST /users/ - Create a user
 GET /users/ - Get all users
 PATCH /users/{id}/deactivate - Deactivate user
Books
 POST /books/ - Add a book
 PATCH /books/{id}/unavailable - Mark as unavailable
Borrows
 POST /borrows/ - Borrow a book
 POST /borrows/{id}/return - Return a book
