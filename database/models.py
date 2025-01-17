from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, TIMESTAMP, Boolean, CHAR, DECIMAL
from sqlalchemy import select

engine = create_async_engine(
    url='sqlite+aiosqlite:///db.sqlite3',
    echo=True
)

session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class MainTable(Base):
    __tablename__ = 'main_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    chat_id = mapped_column(BigInteger)
    expired = TIMESTAMP
    active: Mapped[bool] = mapped_column(Boolean)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    username = mapped_column(CHAR)
    first_name = mapped_column(CHAR)
    last_name = mapped_column(CHAR)
    date = mapped_column(TIMESTAMP)


class Action(Base):
    __tablename__ = 'actions'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    chat_id = mapped_column(BigInteger)
    action = mapped_column(CHAR)
    paid = mapped_column(DECIMAL)
    time_add = mapped_column(BigInteger)


class Chat(Base):
    __tablename__ = 'chats'

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id = mapped_column(BigInteger)
    title = mapped_column(CHAR)
    date = mapped_column(TIMESTAMP)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)