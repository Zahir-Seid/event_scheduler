# 🗓️ Event Scheduler App

A full-stack **Recurring Event Scheduler** that allows users to create, edit, delete, and cancel both one-time and complex recurring events.

Built with:
- **Backend:** Django 5 + Django REST Framework (JWT auth)
- **Frontend:** Vue Js
- **Containerized:** Docker + Docker Compose for simplified local setup

---

## 📁 Project Structure
``` bash
├── Backend/ # Django app (API server)
│ ├── accounts/ # JWT-based authentication
│ ├── events/ # Core event + recurrence logic
│ ├── event_scheduler/ # Main project settings
│ ├── manage.py
│ └── requirements.txt
│
├── FrontEnd/ # Nuxt 3 frontend (Vue 3 + Vite)
│ ├── src/
│ │ ├── pages/ # Event views (create, list, edit)
│ │ ├── components/
│ │ └── layouts/
│ └── package.json
│
├── docker-compose.yml # Orchestrates frontend and backend
└── README.md
```

---

## 🚀 Features

- JWT-authenticated user sessions
- Create one-time or recurring events
- Supports daily, weekly, monthly, and yearly patterns
- Cancel single occurrences without deleting the entire series
- Fully responsive frontend UI 

---

## 🐳 Setup with Docker

> ⚠️ Prerequisites: Docker & Docker Compose must be installed

```bash
# Step 1: Clone the repo
git clone https://github.com/ZAhir-Seid/event-scheduler.git
cd event-scheduler

# Step 2: Build and run services
docker-compose up --build

# Backend: http://localhost:8000/
# Frontend: http://localhost:3000/
```
The backend will auto-migrate and use SQLite for local testing.
## Authentication

    Signup and login via JWT

    Auth token stored in cookies (HTTP-only)

    Protected API endpoints require JWT Bearer token

## Frontend Stack

    Vue js 

    Vite for fast development builds

    Conditional rendering for recurrence rule inputs


## Environment Variables

Create a .env file for frontend.

Frontend .env example:

VITE_API_BASE_URL=http://127.0.0.1:8000/api

## Usage

### From the UI, users can:

    ✅ Create a new event (one-time or recurring)

    📆 Define recurrence patterns (daily, weekly, monthly, yearly)

    🗒️ View all events in a list

    ✂️ Cancel individual occurrences

    🖊️ Edit or delete existing events

## License

MIT — free to use and modify.





