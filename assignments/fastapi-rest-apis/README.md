# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice route design, request handling, and JSON responses. By the end of this assignment, you will create endpoints to read, add, and update resources in a small in-memory dataset.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI app and implement basic endpoints for working with a list of books. Your API should include a health route plus endpoints to list all books and fetch a single book by ID.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Implement `GET /` that returns a short API status message.
- Implement `GET /books` that returns all books as JSON.
- Implement `GET /books/{book_id}` that returns one book when found.
- Return a clear `404` error message when `book_id` does not exist.


### 🛠️	Add Create and Update Behavior

#### Description
Expand the API so users can add a new book and update an existing one using request bodies. Use Pydantic models to validate incoming data.

#### Requirements
Completed program should:

- Define a Pydantic model with `title`, `author`, and `published_year` fields.
- Implement `POST /books` to add a new book and assign it an ID.
- Implement `PUT /books/{book_id}` to update an existing book.
- Return the created or updated book in the response body.
- Return a clear `404` error message when updating a missing `book_id`.
