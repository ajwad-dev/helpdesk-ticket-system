# 🎫 IT Helpdesk Ticket Management System

A containerized IT Helpdesk Ticket Management System built to simulate a real-world internal IT support environment.

The system provides a REST API for creating and managing support tickets, with PostgreSQL used for persistent data storage.

## 🚀 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- Git & GitHub
- Linux

## 🏗️ Architecture

```text
              Client
                │
                ▼
        ┌───────────────┐
        │   FastAPI App │
        │   Container   │
        └───────┬───────┘
                │
         Docker Network
                │
                ▼
        ┌───────────────┐
        │  PostgreSQL   │
        │   Container   │
        └──────────────┘

"" Features
Create and manage IT support tickets
REST API using FastAPI
PostgreSQL database integration
SQLAlchemy ORM
Dockerized application
Multi-container setup with Docker Compose
Container-to-container communication
Persistent database storage
Environment-based configuration
📁 Project Structure
helpdesk-ticket-system/
│
├── app/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
🐳 How to Run

Clone the repository:

git clone https://github.com/ajwad-dev/helpdesk-ticket-system.git
cd helpdesk-ticket-system

Start the application:

docker compose up --build

Check running containers:

docker compose ps

Stop the application:

docker compose down
🔄 How It Works
docker compose up
        ↓
Application + PostgreSQL containers start
        ↓
Docker Network connects the services
        ↓
FastAPI communicates with PostgreSQL
        ↓
Tickets are stored in the database
📚 What I Learned

This project gave me practical experience with:

Docker containerization
Docker Compose
Multi-container applications
Docker networking
Persistent storage
Environment configuration
Running and managing services in Linux

Most importantly, I learned how an application and its database can run as separate containers while communicating through a Docker network.

👨 Author

Ajwad Sultan

GitHub: @ajwad-dev

