from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from apps.core.dependencies import get_session
from .schemas import UserCreate, UserRead, TempEmailModel
from .services import (create_user,
                       get_all_users,
                       update_user_by_id,
                       get_user_by_id,
                       delete_user_by_id)
from pydantic import ValidationError


router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_new_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_session)
):
    try:
        TempEmailModel(email=user.email)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid email: {user.email}"
        )

    return await create_user(db, user)


@router.get("", response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def get_users(db: AsyncSession = Depends(get_session)):
    users = await get_all_users(db=db)
    return users


@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.put("/{user_id}", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
async def update_user(
        user_id: int,
        user: UserCreate,
        db: AsyncSession = Depends(get_session)):

    try:
        TempEmailModel(email=user.email)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid email: {user.email}"
        )

    user = await update_user_by_id( db,user_id, user, )

    if user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session)) ->None:
    await delete_user_by_id( db, user_id)
    return None






