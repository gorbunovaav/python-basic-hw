"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import(
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import MetaData

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 10

SQLALCHEMY_NAMING_CONVENTION: dict[str, str] = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

engine = create_async_engine(
    url = PG_CONN_URI,
    echo = SQLALCHEMY_ECHO,
    pool_size = SQLALCHEMY_POOL_SIZE,
    max_overflow = SQLALCHEMY_MAX_OVERFLOW,
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit = False
    )

Base = DeclarativeBase()
Session = AsyncSession()

class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention = SQLALCHEMY_NAMING_CONVENTION
    )

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    posts = Mapped[List["Post"]] = relationship(back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    body: Mapped[str] = mapped_column(String, nullable=False)
    user: Mapped["Post"] = relationship(back_populates="posts")
