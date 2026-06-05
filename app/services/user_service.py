from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        full_name=user.full_name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(
        User.id == user_id
    ).first()


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user