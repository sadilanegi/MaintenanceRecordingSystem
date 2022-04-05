from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DB_URL ="postgresql://fysczrqlhapjuu:0ce46adf36f60066509dc59e0f97116e3309c8250edcaf60209662974d0b3a5c@ec2-52-3-60-53.compute-1.amazonaws.com:5432/d25djsm4dt2pva"
#SQLALCHEMY_DB_URL ="postgresql://sumit:root@localhost/maintenance_recording"
engine = create_engine(SQLALCHEMY_DB_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
#SQLALCHEMY_DATABASE_URL = "postgresql://sumit:root@localhost/maintenance_recording"


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()