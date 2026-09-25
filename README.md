# Student Management API

A RESTful Student Management API built with **Python, Flask, SQLAlchemy, SQLite, and JWT authentication**.

The project follows a layered architecture to keep API routes, business logic, validation, and database operations separated.

## Features

* User registration and login
* JWT-based authentication
* Password hashing
* Student CRUD operations
* Course management
* Student search by name, email, or course
* Pagination
* Filter students by course
* Input validation
* Custom exception handling
* SQLAlchemy ORM
* SQLite database
* Automated API tests using Pytest
* Flask-Migrate database migrations

## Technologies Used

* Python
* Flask
* SQLAlchemy
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Flask-Migrate
* SQLite
* Pytest
* Postman

## Project Architecture

```text
Client / Postman
       ↓
Flask Routes
       ↓
Services
       ↓
Repositories
       ↓
SQLAlchemy
       ↓
SQLite Database
```

### Main Layers

**Routes**
Handle HTTP requests, JSON data, authentication, and responses.

**Services**
Handle application logic, validation, and coordination between components.

**Repositories**
Handle database operations.

**Models**
Define database tables and their relationships.

**Validators**
Validate incoming student data.

## Project Structure

```text
StudentManagementAPI/
│
├── app/
│   ├── models/
│   ├── services/
│   ├── validators/
│   ├── database/
│   ├── routes/
│   └── exceptions/
│
├── tests/
│
├── data/
│
├── migrations/
│
├── .gitignore
├── requirements.txt
├── .env
└── run.py
```

## API Endpoints

### Authentication

| Method | Endpoint    | Description           |
| ------ | ----------- | --------------------- |
| POST   | `/register` | Register a user       |
| POST   | `/login`    | Login and receive JWT |

### Students

| Method | Endpoint                    | Description     |
| ------ | --------------------------- | --------------- |
| POST   | `/students`                 | Create student  |
| GET    | `/students`                 | Get students    |
| GET    | `/students/<id>`            | Get one student |
| GET    | `/students/search?keyword=` | Search students |
| PUT    | `/students/<id>`            | Update student  |
| DELETE | `/students/<id>`            | Delete student  |

### Courses

| Method | Endpoint        | Description     |
| ------ | --------------- | --------------- |
| POST   | `/courses`      | Create course   |
| GET    | `/courses`      | Get all courses |
| GET    | `/courses/<id>` | Get one course  |

Student and course endpoints require JWT authentication.

## Authentication

After logging in, the API returns an access token.

Send it with protected requests using:

```text
Authorization: Bearer <your-token>
```

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd StudentManagementAPI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate it

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```text
SECRET_KEY=your-secret-key
```

Do not commit `.env` to GitHub.

### 6. Run the application

```bash
python run.py
```

The API will start locally.

## Running Tests

Run the complete automated test suite:

```bash
python -m pytest
```

The tests use an isolated in-memory SQLite database so they do not modify the development database.

## Database Migrations

This project uses Flask-Migrate for database schema migrations.

Typical commands:

```bash
flask --app run.py db migrate -m "Migration message"
flask --app run.py db upgrade
```

## What I Learned

This project helped me practice:

* Building REST APIs with Flask
* Layered application architecture
* SQLAlchemy ORM
* Database relationships and foreign keys
* CRUD operations
* JWT authentication
* Password hashing
* Input validation
* Exception handling
* Database migrations
* API testing with Pytest
* Testing authenticated endpoints
* Using Postman for API testing
* Structuring a maintainable Python project

## Author

**Krishna Patil**

Python Developer / Python Automation Engineer
