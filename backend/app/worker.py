from celery import Celery

from app.core.config import settings
from app.db import SessionLocal
from app.models import Job, JobStatus

celery_app = Celery("teodol", broker=settings.redis_url, backend=settings.redis_url)


@celery_app.task
def process_job(job_id: int):
    db = SessionLocal()
    job = db.get(Job, job_id)
    try:
        job.status = JobStatus.processing
        db.commit()
        # TODO: dispatch on job.kind (ffmpeg, Whisper, TTS) and update job.progress
        job.progress = 100
        job.status = JobStatus.completed
    except Exception:
        job.status = JobStatus.failed
        # TODO: refund job.token_cost to the user
    finally:
        db.commit()
        db.close()
