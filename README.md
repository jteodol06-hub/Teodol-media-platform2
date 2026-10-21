# Teodol

Media platform: text to audio, video to text, subtitles, summaries and more.

## Stack
Next.js + TypeScript + Tailwind (frontend) | FastAPI + SQLAlchemy (backend) | PostgreSQL | Redis + Celery (jobs)

## Run locally
1. `cp .env.example .env` and fill in the values
2. `docker compose up --build`
3. Frontend: http://localhost:3000 | API docs: http://localhost:8000/docs

## Layout
- `backend/app/core` config, security helpers
- `backend/app/routers` API routes
- `backend/app/worker.py` background job processing
- `frontend/src/app` pages | `frontend/src/components` UI
