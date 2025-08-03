
# User Management API (Refactored)

A secure and modular Flask-based User Management API. This project refactors a legacy monolithic API into a well-structured, maintainable, and safer application.

---

## Features

- Modular Flask application using Blueprints
- Secure password hashing (no plaintext storage)
- Protection from SQL injection via parameterized queries
- RESTful endpoints for full user CRUD operations
- Basic login and search functionality
- Clean JSON responses with proper status codes

---

## Installation & Setup

### Prerequisites

- Python 3.8+ installed
- `pip` package manager
- SQLite (bundled with Python)
- Postman (optional for testing)

### Steps to Run

1. **Navigate to the project**:
   ```bash
   cd path/to/messy-migration-refactored
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   # OR
   source venv/bin/activate   # Mac/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install flask werkzeug
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Start the server**:
   ```bash
   python app.py
   ```

API will run at: `http://127.0.0.1:5009`

---

## API Usage

### 1. GET / — Health Check
```
GET http://127.0.0.1:5009/
```

### 2. POST /users — Create a New User
```json
POST http://127.0.0.1:5009/users
{
  "name": "Alice",
  "email": "alice@example.com",
  "password": "securepassword"
}
```

### 3. GET /users — List All Users
```
GET http://127.0.0.1:5009/users
```

### 4. GET /user/<id> — Fetch Single User
```
GET http://127.0.0.1:5009/user/1
```

### 5. PUT /user/<id> — Update a User
```json
PUT http://127.0.0.1:5009/user/1
{
  "name": "Alice Updated",
  "email": "alice.updated@example.com"
}
```

### 6. DELETE /user/<id> — Remove a User
```
DELETE http://127.0.0.1:5009/user/1
```

### 7. GET /search?name=Alice — Search Users
```
GET http://127.0.0.1:5009/search?name=Alice
```

### 8. POST /login — Login
```json
POST http://127.0.0.1:5009/login
{
  "email": "alice@example.com",
  "password": "securepassword"
}
```

---

## Notes

- Use [Postman](https://www.postman.com/) or curl to test endpoints.
- Ensure you run `init_db.py` before using `/users` routes.

---

## AI Usage Disclosure

- ChatGPT was used to assist with:
  - Generating route and service boilerplate
  - Drafting project documentation (e.g., CHANGES.md, usage instructions)

- All outputs were reviewed and tested manually to ensure accuracy and relevance.
