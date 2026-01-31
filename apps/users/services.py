from sqlalchemy.orm import Session
from .models import UserModel
from .schemas import User


def create_user(db: Session, user: User):
    db_user = UserModel(
        name=user.name,
        email=user.email,
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user