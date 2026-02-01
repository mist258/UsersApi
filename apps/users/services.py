from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from apps.users.models import User
from apps.users.schemas import UserCreate
from typing import Sequence
from sqlalchemy import select


async def create_user(db: AsyncSession,
                      user: UserCreate
                      ) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def update_user_by_id(db: AsyncSession,
                      user_id: int,
                      data: UserCreate) -> User:
    stmt =  select(User).where(User.id == user_id)
    result = await db.scalars(stmt)
    user = result.first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    updated_user = data.model_dump(exclude_unset=True)
    for key, value in updated_user.items():
        setattr(user, key, value)

    await db.commit()
    await db.refresh(user)
    return user


async def get_all_users(db: AsyncSession
                        )-> Sequence[User]:

    stmt = select(User).order_by(User.id)
    result = await db.scalars(stmt)
    return result.all()


async def get_user_by_id(db: AsyncSession,
                      user_id: int) -> User:
    stmt = select(User).where(User.id == user_id)
    result = await db.scalar(stmt)
    return result


async def delete_user_by_id(db: AsyncSession,
                            user_id: int) -> None:
    stmt = select(User).where(User.id == user_id)
    user = await db.scalar(stmt)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    await db.delete(user)
    await db.commit()
