# HabitXP API 🌿

The FastAPI backend for HabitXP — a mobile habit tracking app with analytics, streaks, and gamified achievements.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Python 3.15 + FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Task Queue | Celery |
| Cache/Broker | Redis |
| Auth | Firebase Admin SDK (Google OAuth) |
| Validation | Pydantic |
| Password | Passlib |
| Tokens | Python-Jose (JWT) |

---

## Getting Started

### Prerequisites
- Python 3.15+
- PostgreSQL running locally or on Railway/Supabase
- Redis running locally or on Railway

### Create and activate virtual environment

```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary python-dotenv celery redis python-jose passlib
```

### Run the server

```bash
uvicorn main:app --reload
```

- API live at: `http://localhost:8000`
- Interactive docs at: `http://localhost:8000/docs`
- ReDoc at: `http://localhost:8000/redoc`

---

## Project Structure

```
habitxp-api/
├── app/
│   ├── routers/            # API endpoint files
│   │   ├── __init__.py
│   │   ├── users.py        # User endpoints
│   │   ├── habits.py       # Habit CRUD endpoints
│   │   ├── logs.py         # Habit logging endpoints
│   │   ├── streaks.py      # Streak endpoints
│   │   └── achievements.py # Achievement endpoints
│   ├── models/             # SQLAlchemy table definitions
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── habit.py
│   │   ├── habit_log.py
│   │   ├── streak.py
│   │   ├── notification.py
│   │   ├── achievement.py
│   │   └── user_achievement.py
│   ├── schemas/            # Pydantic request/response shapes
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── habit.py
│   │   └── achievement.py
│   ├── services/           # Business logic
│   │   ├── __init__.py
│   │   ├── streak_service.py       # Streak calculation
│   │   └── achievement_service.py  # Achievement checking
│   ├── db/                 # Database connection
│   │   ├── __init__.py
│   │   └── session.py
│   └── __init__.py
├── celery_worker/          # Async task definitions
├── alembic/                # Database migrations
├── main.py                 # FastAPI app entry point
├── .env                    # Environment variables (never commit)
├── .gitignore
└── requirements.txt
```

---

## Database Schema

| Table | Description |
|---|---|
| `users` | User accounts and preferences |
| `habits` | Habit definitions per user |
| `habit_logs` | Daily log entries per habit |
| `streaks` | Current and longest streak per habit |
| `notifications` | Notification schedule per habit |
| `achievements` | Static lookup table of all 30 achievements |
| `user_achievements` | Achievements earned by each user |

### Key Indexes
- `habit_logs (habit_id, logged_date)` — dashboard queries
- `user_achievements (user_id, achievement_id)` — prevent duplicates
- `streaks (habit_id)` — frequent dashboard reads

---

## Environment Variables

Create a `.env` file in the root:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/habitxp
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key_here
FIREBASE_PROJECT_ID=your_firebase_project_id
```

---

## API Endpoints (Planned)

```
POST   /auth/google          # Google OAuth login
GET    /users/me             # Get current user

GET    /habits               # List all habits
POST   /habits               # Create a habit
PUT    /habits/{id}          # Update a habit
DELETE /habits/{id}          # Delete a habit
PATCH  /habits/{id}/archive  # Archive a habit

POST   /logs                 # Log a habit for today
GET    /logs/{habit_id}      # Get logs for a habit

GET    /streaks/{habit_id}   # Get streak for a habit

GET    /achievements         # List all achievements
GET    /achievements/me      # Get user's earned achievements

GET    /stats/dashboard      # Overall dashboard stats
GET    /stats/heatmap/{habit_id}  # Heatmap data for a habit
```

---

## Running Celery (Task Queue)

In a separate terminal with your venv activated:

```bash
celery -A celery_worker worker --loglevel=info
```

Celery handles:
- Checking achievements after every habit log
- Sending push notifications at scheduled times
- End-of-day reminders for unlogged habits

---

## Related

- [HabitXP](https://github.com/YOURUSERNAME/habitxp) — React Native frontend
