"""Starter code for the Building REST APIs with FastAPI assignment.

Run locally with:
uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory dataset for assignment practice.
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "published_year": 2008},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "published_year": 1999},
]


class BookInput(BaseModel):
    title: str
    author: str
    published_year: int


@app.get("/")
def root():
    # TODO: Return a short API status message.
    return {"message": "TODO"}


@app.get("/books")
def get_books():
    # TODO: Return all books.
    return []


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return matching book or raise 404.
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: BookInput):
    # TODO: Create a new book with a generated ID and return it.
    return {}


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update matching book or raise 404.
    raise HTTPException(status_code=404, detail="Book not found")
