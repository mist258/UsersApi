from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from .schemas import User
from apps.core.dependencies import get_db
from .services import create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=User)
async def create_new_user(user: User, db: Session = Depends(get_db)):
   return create_user(db, user)


