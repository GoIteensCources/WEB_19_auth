from sqlalchemy import ForeignKey, String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from settings import Session

from flask_login import UserMixin

from settings import Base


class User(UserMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(String(200), nullable=False)


    is_admin: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"User: {self.id}, {self.username}"
    
    @staticmethod
    def get(user_id: int) :
        with Session() as session:
            user = session.scalar(select(User).filter(User.id == user_id))
            return user
        

    @classmethod
    def get_by_username(cls, username: str) :
        with Session() as session:
            user = session.scalar(select(cls).filter(cls.username == username))
            return user
        