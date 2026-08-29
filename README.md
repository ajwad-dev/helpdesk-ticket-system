# 🎫 IT Helpdesk Ticket Management System

A containerized **IT Helpdesk Ticket Management System** built to simulate a real-world internal IT support environment.

The application provides a REST API for creating and managing support tickets, with **PostgreSQL** used for persistent data storage. The application and database run as separate Docker containers and communicate through a private Docker network.

---

## 🚀 Tech Stack

| Technology     | Purpose                                |
| -------------- | -------------------------------------- |
| Python         | Application development                |
| FastAPI        | REST API framework                     |
| PostgreSQL     | Relational database                    |
| SQLAlchemy     | ORM and database interaction           |
| Docker         | Application containerization           |
| Docker Compose | Multi-container orchestration          |
| Git & GitHub   | Version control                        |
| Linux          | Development and deployment environment |

---

## 🏗️ Architecture

```text
                    Client
                      │
                      │ HTTP
                      ▼
             ┌─────────────────┐
             │    FastAPI      │
             │   Application   │
             │    Container    │
             └────────┬────────┘
                      │
                      │ PostgreSQL
                      │ Docker Network
                      ▼
             ┌─────────────────┐
             │   PostgreSQL    │
             │    Database     │
             │    Container    │
             └────────┬────────┘
                      │
                      ▼
                Docker Volume
             Persistent Database
                   Storage
```

### How the architecture works

* The **FastAPI application** runs inside its own container.
* **PostgreSQL** runs inside a separate container.
* Docker Compose creates a private network for communication between services.
* FastAPI connects to PostgreSQL using the Docker service name.
* PostgreSQL data is stored in a Docker volume so that data persists across container restarts.

---

## ✨ Features

* Create and manage IT support tickets
* RESTful API built with FastAPI
* PostgreSQL database integration
* SQLAlchemy ORM
* Dockerized application
* Multi-container architecture
* Docker Compose orchestration
* Container-to-container networking
* Persistent database storage
* Environment-based configuration
* Health checks for services

---

## 📁 Project Structure

```text
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
```

---

## 🐳 Getting Started

### Prerequisites

Make sure you have the following installed:

* Docker
* Docker Compose
* Git

### 1. Clone the repository

```bash
git clone https://github.com/ajwad-dev/helpdesk-ticket-system.git
cd helpdesk-ticket-system
```

### 2. Start the application

Build the Docker image and start both services:

```bash
docker compose up --build
```

The application will start with:

```text
FastAPI
    │
    └── PostgreSQL
```

### 3. Check running containers

```bash
docker compose ps
```

### 4. Access the API

Open:

```text
http://localhost:8000
```

FastAPI interactive API documentation is available at:

```text
http://localhost:8000/docs
```

### 5. Stop the application

```bash
docker compose down
```

> Database data is preserved through the Docker volume unless the volume is explicitly removed.

---

## 🔄 Application Workflow

```text
docker compose up
        │
        ▼
Build FastAPI Image
        │
        ▼
Start FastAPI Container
        │
        ▼
Start PostgreSQL Container
        │
        ▼
Docker Compose Network
        │
        ▼
FastAPI ───────────► PostgreSQL
        │
        ▼
Create / Manage Tickets
        │
        ▼
Store Data in PostgreSQL
```

---

## 🌐 Container Networking

The application and database communicate using Docker's internal network.

```text
FastAPI Container
       │
       │ postgres:5432
       ▼
PostgreSQL Container
```

The FastAPI container does **not** need to connect to PostgreSQL through `localhost`.

Instead, Docker Compose provides service discovery using the PostgreSQL service name:

```text
postgres
```

Therefore, the application can connect using:

```text
HOST=postgres
PORT=5432
```

---

## 💾 Persistent Storage

PostgreSQL uses a Docker volume to persist database data.

```text
PostgreSQL Container
        │
        ▼
  Docker Volume
        │
        ▼
Persistent Database Data
```

This means removing and recreating the PostgreSQL container does not automatically delete the stored database data.

---

## 📚 What I Learned

This project provided hands-on experience with:

* Docker images and containers
* Writing Dockerfiles
* Docker Compose
* Multi-container applications
* Docker networking
* Container-to-container communication
* PostgreSQL in Docker
* Docker volumes and persistent storage
* Environment variables
* Application health checks
* Linux-based application management
* Git and GitHub workflow

### Key DevOps Concept

The most important concept demonstrated by this project is that an application and its database do **not** need to run in the same container.

Instead:

```text
Application Container
        │
        │ Docker Network
        ▼
Database Container
```

Each service has its own responsibility while Docker Compose manages the overall application stack.

---

## 👨‍💻 Author

**Ajwad Sultan**

GitHub: [@ajwad-dev](https://github.com/ajwad-dev)

---

## 📌 Project Status

🚧 **Educational / Portfolio Project**

This project is being developed as part of a hands-on journey into **Docker, DevOps, cloud infrastructure, and deployment automation**.
