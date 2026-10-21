from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Job, JobKind, User
from app.worker import process_job

router = APIRouter(prefix="/jobs", tags=["jobs"])

COST = {JobKind.text_to_audio: 1, JobKind.video_to_text: 5}


def get_current_user(db: Session = Depends(get_db)) -> User:
    # TODO: replace with your existing auth (JWT + verified email)
    user = db.get(User, 1)
    if not user:
        raise HTTPException(401, "Not authenticated")
    return user


class JobIn(BaseModel):
    kind: JobKind
    input_key: str = ""


@router.post("", status_code=201)
def create_job(body: JobIn, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    cost = COST.get(body.kind, 1)
    if user.tokens < cost:
        raise HTTPException(402, "Not enough tokens")
    user.tokens -= cost
    job = Job(user_id=user.id, kind=body.kind, input_key=body.input_key, token_cost=cost)
    db.add(job)
    db.commit()
    process_job.delay(job.id)
    return {"id": job.id, "status": job.status}


@router.get("")
def list_jobs(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    rows = db.scalars(select(Job).where(Job.user_id == user.id).order_by(Job.id.desc()).limit(50))
    return [{"id": j.id, "kind": j.kind, "status": j.status, "progress": j.progress} for j in rows]
