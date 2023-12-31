import streamlit as st

books = []  # List to store book data
users = {}  # Dictionary to store user accounts

def main():
    st.title("Collaborative Online Book Store")

    login_state = get_login_state()

    if not login_state["logged_in"]:
        login_page(login_state)
        st.stop()

    operation = st.sidebar.selectbox("Operation", ["View Books", "Order Books", "Manage Books"])

    if operation == "View Books":
        view_books()
    elif operation == "Order Books":
        order_books()
    elif operation == "Manage Books":
        manage_books()

def get_login_state():
    login_state = {"logged_in": False, "username": None}

    if "login_state" in st.session_state:
        login_state = st.session_state.login_state

    return login_state

def set_login_state(logged_in, username):
    st.session_state.login_state = {"logged_in": logged_in, "username": username}

def login(username, password):
    if username in users and users[username] == password:
        set_login_state(True, username)
        return True
    return False

def logout():
    set_login_state(False, None)

def register(username, password):
    if username in users:
        return False

    users[username] = password
    set_login_state(True, username)
    return True

def login_page(login_state):
    st.header("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success("Logged in successfully.")
        else:
            st.error("Invalid username or password.")

    st.markdown("---")

    st.header("Register")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Register"):
        if register(new_username, new_password):
            st.success("Registered and logged in successfully.")
        else:
            st.error("Username already taken.")

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
