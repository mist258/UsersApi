from pydantic import BaseModel,EmailStr


class UserCreate(BaseModel):
    name: str
    email: str


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


class TempEmailModel(BaseModel):
    email: EmailStr


