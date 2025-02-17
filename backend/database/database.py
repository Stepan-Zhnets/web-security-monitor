from sqlalchemy import create_engine
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///database.db"
LOCATIONS_DATABASE_URL = "sqlite:///locations.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
location_engine = create_engine(LOCATIONS_DATABASE_URL,
                                connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
SessionLocanLocation = sessionmaker(autocommit=False,
                                    autoflush=False,
                                    bind=location_engine)

Base = declarative_base()

#|==================================================|



#|==================================================|

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

