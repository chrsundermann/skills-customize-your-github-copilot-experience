# 📘 Assignment: Frontend API Integration Dashboard

## 🎯 Objective

Build a browser-based dashboard that consumes a FastAPI backend and displays live data to users. In this assignment, you will practice asynchronous JavaScript, DOM updates, and handling API errors in a realistic full-stack workflow.

## 📝 Tasks

### 🛠️	Render Data from FastAPI Endpoints

#### Description
Use `fetch` in JavaScript to call the FastAPI books endpoints and render the returned data in the browser. Start from the provided starter files and connect the UI to your existing API.

#### Requirements
Completed program should:

- Use `starter-app.js` to call `GET /books` from a FastAPI server.
- Render each book in the dashboard with title, author, and year.
- Show a visible loading message while data is being fetched.
- Display a clear error message if the API request fails.
- Keep API base URL configurable in one constant variable.


### 🛠️	Add Interactive Search and Detail View

#### Description
Improve the dashboard by adding user interactions that help explore the data. Implement a client-side search box and a detail panel loaded from `GET /books/{book_id}`.

#### Requirements
Completed program should:

- Add a text input that filters the displayed book list by title or author.
- Add a "View Details" button for each book card.
- Fetch and display details for the selected book using `GET /books/{book_id}`.
- Keep the page responsive and usable on both desktop and mobile widths.
- Handle not-found responses with a clear message in the detail panel.
