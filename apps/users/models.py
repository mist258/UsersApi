from sqlalchemy import Column, Integer, String, Boolean
from apps.core.database import Base
from sqlalchemy.orm import Mapped


class UserModel(Base):

    id: Mapped[int] = Column(Integer,
                             primary_key=True,
                             index=True,
                             autoincrement=True,
                             nullable=False)
    name: Mapped[str] = Column(String(40),
                               nullable=False)
    email: Mapped[str] = Column(String(40),
                                unique=True,
                                nullable=False)
    is_active: Mapped[bool] = Column(Boolean,
                                     default=True,
                                     nullable=False)

    def __repr__(self) -> str:
        return (f"Address(id={self.id!r}, "
                f"name={self.name!r}, "
                f"email={self.email!r}, "
                f"is_active={self.is_active!r} )")
