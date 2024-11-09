"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from datetime import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Post
from models.db_async import engine, async_session

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def create_user(
    session: AsyncSession,
    name: str,
    username: str,
    email: str,
) -> User:
    owner = User(
        name=name,
        username=username,
        email=email,
    )
    session.add(owner)
    await session.commit()
    # await session.refresh(owner)
    return owner

async def create_post(
    session: AsyncSession,
    title: str,
    body: str,
) -> Post:
    post = Post(
        title=title,
        body=body,
    )
    session.add(post)
    await session.commit()
    # await session.refresh(owner)
    return post


async def main():
  users_data, posts_data = await asyncio.gather(
    create_user(),
    create_post(),
    )

if __name__ == "__main__":
    asyncio.run(main())
