import streamlit as st
import json
import os

# File to store book data
BOOKS_FILE = "books.json"

# Initialize books.json if not exists
def initialize_data():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w") as file:
            json.dump([], file)

# Load books from JSON
def load_books():
    with open(BOOKS_FILE, "r") as file:
        return json.load(file)

# Save books to JSON
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Add a new book
def add_book(title, author, status="Available"):
    books = load_books()
    books.append({"title": title, "author": author, "status": status})
    save_books(books)
    st.success(f'Book "{title}" added successfully!')

# Search books
def search_books(query):
    books = load_books()
    results = [book for book in books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
    return results

# Borrow a book
def borrow_book(title):
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower() and book["status"] == "Available":
            book["status"] = "Borrowed"
            save_books(books)
            st.success(f'You have borrowed "{title}"!')
            return
    st.error("Book is either not available or already borrowed.")

# Return a book
def return_book(title):
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower() and book["status"] == "Borrowed":
            book["status"] = "Available"
            save_books(books)
            st.success(f'You have returned "{title}"!')
            return
    st.error("Book is either not borrowed or does not exist.")

# Streamlit UI
def main():
    st.title("📚 Library Management System")
    
    menu = ["Add Book", "Search Book", "Borrow Book", "Return Book"]
    choice = st.sidebar.selectbox("Choose an option", menu)
    
    if choice == "Add Book":
        st.subheader("Add a New Book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        if st.button("Add Book"):
            if title and author:
                add_book(title, author)
            else:
                st.error("Please enter both title and author.")
    
    elif choice == "Search Book":
        st.subheader("Search for Books")
        query = st.text_input("Enter Title or Author")
        if st.button("Search"):
            results = search_books(query)
            if results:
                for book in results:
                    st.write(f'**{book["title"]}** by {book["author"]} - *{book["status"]}*')
            else:
                st.warning("No books found.")
    
    elif choice == "Borrow Book":
        st.subheader("Borrow a Book")
        title = st.text_input("Enter Book Title")
        if st.button("Borrow"):
            borrow_book(title)
    
    elif choice == "Return Book":
        st.subheader("Return a Book")
        title = st.text_input("Enter Book Title")
        if st.button("Return"):
            return_book(title)

if __name__ == "__main__":
    initialize_data()
    main()
