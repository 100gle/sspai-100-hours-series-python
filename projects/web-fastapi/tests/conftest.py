import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

# isort: off
from popup_api.main import app
from popup_api.settings import settings


engine = create_engine(
    url=settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    connect_args=settings.DATABASE_CONNECT_ARGS,
)
TestSession = sessionmaker(bind=engine)


@pytest.fixture(scope="package")
def client():
    yield TestClient(app)


@pytest.fixture()
def db():
    sess = TestSession()
    try:
        yield sess
    finally:
        sess.close()
