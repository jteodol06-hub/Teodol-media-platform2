# 🎙️ Teodol Media Platform

A robust, full-stack media processing web application designed to handle advanced audio and video workflows—including text-to-audio conversion, video transcription, automated subtitle generation, intelligent summaries, and more.

## ✨ Features

- Text-to-Audio: Convert written documents or notes into natural-sounding audio files.

- Video-to-Text Transcription: Accurately transcribe spoken dialogue from video files.

- Automated Subtitles: Generate timed subtitle tracks for media content.

- Content Summaries: Condense lengthy transcripts and documents into concise summaries.

- Background Processing: Powered by Celery and Redis to handle heavy media workloads asynchronously without blocking the UI.

## 🛠️ Tech Stack

- Frontend: Next.js, TypeScript, Tailwind CSS

- Backend: FastAPI, SQLAlchemy, Python

- Database: PostgreSQL

- Task Queue & Caching: Redis, Celery

- Containerization: Docker & Docker Compose

  ## 📁 Project Layout
```text
.
├── backend/
│   └── app/
│       ├── core/         # Configuration and security helpers
│       ├── routers/      # API route endpoints
│       └── worker.py     # Background job processing (Celery)
├── frontend/
│   └── src/
│       ├── app/          # Next.js pages and routing
│       └── components/   # Reusable UI components
├── docker-compose.yml
└── README.md
```

## 🚀 Running Locally

- Follow these instructions to get the application up and running on your local machine using Docker.

### Prerequisites

Ensure you have Docker and Docker Compose installed on your system.

### Setup Steps

1. Clone the repository:
   - git clone https://github.com/jteodol06-hub/Teodol-media-platform2.git
cd Teodol-media-platform2

2. Configure environment variables:
Copy the example environment file and fill in your custom configurations:
   - cp .env.example .env
(Open the newly created .env file and add your database URLs, secret keys, and any external API credentials).

3. Build and start the containers:
   - docker compose up --build

4. Access the application:

Frontend UI: http://localhost:3000

Backend API Docs (Swagger): http://localhost:8000/docs

## Layout
- `backend/app/core` config, security helpers
- `backend/app/routers` API routes
- `backend/app/worker.py` background job processing
- `frontend/src/app` pages | `frontend/src/components` UI
## 📄 License
This project is open-source and available under the MIT License.
