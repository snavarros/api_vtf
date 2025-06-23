import pytest
from app.config.database import get_db
from app.main import app


@pytest.fixture(scope="function")
async def override_get_db(db_session):
    async def _override():
        yield db_session

    app.dependency_overrides[get_db] = _override
    yield
    app.dependency_overrides.pop(get_db, None)


@pytest.fixture(scope="function")
async def db_session():
    from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
    from app.config.database import Base

    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)
    async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        yield session
        await session.rollback()
