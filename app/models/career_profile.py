from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class CareerProfile(Base):

    __tablename__ = "career_profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    skills: Mapped[str] = mapped_column(
        Text()
    )

    projects: Mapped[str] = mapped_column(
        Text()
    )

    education: Mapped[str] = mapped_column(
        Text()
    )

    experience: Mapped[str] = mapped_column(
        Text()
    )