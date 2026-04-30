// Starter JavaScript for the Frontend API Integration Dashboard assignment.

const API_BASE_URL = "http://127.0.0.1:8000";

const statusEl = document.getElementById("status");
const bookListEl = document.getElementById("book-list");
const bookDetailsEl = document.getElementById("book-details");
const searchInputEl = document.getElementById("search");

let books = [];

async function fetchBooks() {
  // TODO: Fetch GET /books and store result in books.
  // TODO: Update status text during loading and error states.
}

function renderBooks(items) {
  // TODO: Render each book in #book-list.
  // TODO: Add a View Details button that calls fetchBookDetails(book.id).
}

async function fetchBookDetails(bookId) {
  // TODO: Fetch GET /books/{book_id} and render in #book-details.
  // TODO: Handle not found and network errors.
}

function setupSearch() {
  // TODO: Filter displayed books by title/author as user types.
}

async function initDashboard() {
  await fetchBooks();
  setupSearch();
}

initDashboard();
