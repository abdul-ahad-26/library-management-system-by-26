Library Management System
Project Overview
This is a simple Library Management System built using Python and Streamlit. It allows librarians to:

Add books by entering the title, author, and availability status.
Search books by title or author.
Borrow books (mark as "Borrowed").
Return books (mark as "Available").
View the current status of all books.
The system stores book data in a JSON file, making it lightweight and easy to manage.

Installation & Setup
Prerequisites
Install uv
Install Python (if not installed)
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/abdul-ahad-26/library-management-system-by-26.git
cd library-management-system
Step 2: Install Dependencies using uv
bash
Copy
Edit
uv venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate      # For Windows
uv pip install -r requirements.txt
Step 3: Run the Application
bash
Copy
Edit
streamlit run app.py
Usage Guide
1. Add a Book
Enter the book title and author.
Select availability status (Available by default).
Click "Add Book" to save it.
2. Search for a Book
Enter a title or author name in the search bar.
The system will display matching books.
3. Borrow a Book
Select a book from the available list.
Click "Borrow" to update the status.
4. Return a Book
Select a borrowed book.
Click "Return" to mark it as Available.
5. View All Books
A table shows all books with their details and current status.
Project Structure
perl
Copy
Edit
library-management-system/
│── app.py               # Main Streamlit app
│── books.json           # Stores book data
│── requirements.txt     # Dependencies
│── README.md            # Documentation
Future Improvements
✔ Add a database (SQLite, PostgreSQL) instead of JSON.
✔ Implement user authentication (admin & users).
✔ Enhance UI design for better user experience.

License
This project is open-source under the MIT License.


