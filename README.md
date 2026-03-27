# Fundoo Notes API – Complete Project Documentation

## Project Overview
Fundoo Notes API is a production-ready FastAPI backend application that allows users to manage accounts and notes with full CRUD operations, database integration, schema validation, and structured logging. The project follows a clean architecture with modular coding practices.

## Features
- User Management: Create, Read, Update, Delete users
- Notes Management: Create, Read, Update, Delete notes
- Database Integration: SQLAlchemy ORM for database management
- Schema Validation: Pydantic schemas for request and response validation
- Structured Logging: Logs API actions and errors to logs/app.log
- Modular Architecture: Separate folders for configuration, models, schemas, services, and routes

## Project Folder Structure
```
fundoo-app/
├── src/
│   ├── config/        # Database and logger configuration
│   ├── models/        # SQLAlchemy models for users and notes
│   ├── schemas/       # Pydantic schemas for request/response validation
│   ├── services/      # Business logic for users and notes
│   ├── router/        # API route endpoints
│   └── main.py        # FastAPI app entry point
├── logs/              # Application logs
│   └── app.log
├── .env               # Environment variables
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Environment Variables (.env)
USER_NAME
PASSWORD
IP
PORT_NUMBER
DATABASE

## Installation & Setup
1. Clone the repository:
   git clone <repository_url>
   cd fundoo-app
2. Install dependencies:
   pip install -r requirements.txt
3. Configure environment variables in .env
4. Run the project:
   uvicorn src.main:app --reload
5. Access Swagger UI: http://127.0.0.1:8000/docs

## API Endpoints

### Users
| Method | Endpoint              | Description           |
|--------|----------------------|---------------------|
| POST   | /users/create         | Create a new user    |
| GET    | /users/all            | Get all users        |
| GET    | /users/{id}           | Get user by ID       |
| PUT    | /users/update/{id}    | Update user by ID    |
| DELETE | /users/delete/{id}    | Delete user by ID    |

### Notes
| Method | Endpoint              | Description           |
|--------|----------------------|---------------------|
| POST   | /notes/create         | Create a new note    |
| GET    | /notes/all            | Get all notes        |
| GET    | /notes/{id}           | Get note by ID       |
| PUT    | /notes/update/{id}    | Update note by ID    |
| DELETE | /notes/delete/{id}    | Delete note by ID    |

## Logging
- All API actions and errors are logged to logs/app.log
- Provides info-level logs and error tracking
- Logging implemented using Loguru

## Final Outcome
- Fully functional User CRUD operations
- Fully functional Notes CRUD operations
- Integrated SQLAlchemy database
- Validated request and response schemas
- Structured logging system
- Clean, modular project architecture

## Use Cases
- Resume / portfolio project
- Backend development practice
- Job interview preparation
- Learning real-world FastAPI project structure

## Author
Shaik Nafisa 
