import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DEFAULT_DATABASE_URL = f"sqlite:///{Path(__file__).with_name('roomhub.db').as_posix()}"
Base = declarative_base()
engine = None
SessionLocal = None


def configure_database(database_url=None):
    global engine, SessionLocal

    if engine is not None:
        engine.dispose()

    url = database_url or os.getenv("ROOMHUB_DATABASE_URL", DEFAULT_DATABASE_URL)
    options = {"check_same_thread": False} if url.startswith("sqlite") else {}
    engine = create_engine(url, connect_args=options)
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    return engine


def init_db():
    from models.moradia import Moradia
    from models.usuario import Usuario

    Base.metadata.create_all(bind=engine)


configure_database()