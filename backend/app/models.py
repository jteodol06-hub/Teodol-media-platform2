import enum
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class JobKind(str, enum.Enum):
    text_to_audio = "text_to_audio"
    video_to_text = "video_to_text"
    audio_to_text = "audio_to_text"
    translate = "translate"
    summarize = "summarize"


class JobStatus(str, enum.Enum):
    queued = "queued"
    processing = "processing"
    completed = "completed"
    failed = "failed"


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    tokens: Mapped[int] = mapped_column(Integer, default=100)


class Job(Base):
    __tablename__ = "jobs"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    kind: Mapped[JobKind] = mapped_column(Enum(JobKind))
    status: Mapped[JobStatus] = mapped_column(Enum(JobStatus), default=JobStatus.queued)
    progress: Mapped[int] = mapped_column(Integer, default=0)
    token_cost: Mapped[int] = mapped_column(Integer, default=0)
    input_key: Mapped[str] = mapped_column(String(500), default="")
    output_key: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
