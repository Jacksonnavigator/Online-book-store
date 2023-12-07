import streamlit as st

books = []  # List to store book data
users = {}  # Dictionary to store user accounts

def main():
    st.title("Collaborative Online Book Store")

    logged_in = False
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        logged_in = login(username, password)
        if not logged_in:
            st.sidebar.error("Invalid username or password.")

    if not logged_in:
        st.stop()

    operation = st.sidebar.selectbox("Operation", ["View Books", "Order Books", "Manage Books"])

    if operation == "View Books":
        view_books()
    elif operation == "Order Books":
        order_books()
    elif operation == "Manage Books":
        manage_books()

def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

def view_books():
    st.header("Available Books")
    
    if len(books) == 0:
        st.write("No books available.")
    else:
        for book in books:
            st.write(f"- {book['title']} by {book['author']}")

def order_books():
    st.header("Order Books")
    

def manage_books():
    st.header("Manage Books")
    

if __name__ == "__main__":
    main()
