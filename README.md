# Django Todo App

A simple and responsive **Todo Management Application** built with **Django**. The application allows users to create, update, delete, search, filter, and manage tasks based on their status, priority, and dates.

## Features

* Create new tasks with title, description, priority, start date, and end date
* Edit existing tasks
* Delete tasks
* Mark tasks as completed or pending
* Search tasks by title or task ID
* Filter tasks by:

  * Created date
  * Start date
  * End date
  * Priority
  * Completion status
* Identify overdue tasks automatically
* Task creation timestamp
* Clean Django template-based interface
* SQLite database for local development
* Production-ready configuration using Gunicorn and WhiteNoise

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Django Templates
* **Database:** SQLite
* **Server:** Gunicorn
* **Static Files:** WhiteNoise

## Project Structure

```text
django_todo/
│
├── task/
│   ├── migrations/
│   ├── templates/
│   │   └── task/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── todo/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Task Model

Each task contains:

| Field         | Description                                |
| ------------- | ------------------------------------------ |
| `title`       | Task title                                 |
| `description` | Detailed task description                  |
| `completed`   | Completion status                          |
| `created_at`  | Automatically generated creation timestamp |
| `start_date`  | Task start date                            |
| `end_date`    | Task deadline                              |
| `priority`    | Task priority level                        |

## Task Operations

The application provides separate routes for the main task operations:

* View all tasks
* Add a task
* Edit a task
* Delete a task
* Filter tasks by priority
* Toggle task completion
* Filter tasks by status

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/akriti04gupta/django_todo.git
cd django_todo
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Filtering & Search

Tasks can be searched using their **title or task ID**. The application also supports filtering based on creation date, start date, end date, priority, and task status.

The status filter includes:

* **Completed Tasks**
* **Overdue Tasks**

An overdue task is identified when its deadline has passed and it has not yet been completed.

## Future Improvements

Some possible improvements for future versions:

* User authentication and user-specific task lists
* REST API using Django REST Framework
* PostgreSQL database
* Task categories/tags
* Pagination
* Sorting by priority and deadline
* Email or browser notifications
* Docker deployment
* Automated test coverage
* Improved responsive UI

## License

This project is intended for learning and development purposes.
