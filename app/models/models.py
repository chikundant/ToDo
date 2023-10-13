import datetime
import uuid
from typing import List

from sqlalchemy import Column, text, UUID
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    __abstract__ = True
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        server_default=text("gen_random_uuid()"),
        default=uuid.uuid4,
    )


projects_users = Table(
    "projects_users",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("project_id", ForeignKey("projects.id")),
)


class User(Base):
    __tablename__ = "users"

    email = Column("email", String, unique=True, nullable=False)
    username = Column("username", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)

    created_tasks: Mapped[List["Task"]] = relationship(
        back_populates="created_by"
    )
    assigned_tasks: Mapped[List["Task"]] = relationship(
        back_populates="assigned_to"
    )

    projects: Mapped[List["Project"]] = relationship(secondary=projects_users)


class Project(Base):
    __tablename__ = "projects"

    tasks: Mapped[List["Task"]] = relationship(back_populates="project_id")
    users: Mapped[List["User"]] = relationship(secondary=projects_users)


class Task(Base):
    __tablename__ = "tasks"

    title = Column("title", String)
    description = Column("description", String)
    created_at = Column(
        "created_at", DateTime, default=datetime.datetime.utcnow()
    )
    status = Column("status", String)

    created_by: Mapped["User"] = ForeignKey("users.id")
    assigned_to: Mapped["User"] = ForeignKey("users.id")
    project_id: Mapped["Project"] = ForeignKey("projects.id")
