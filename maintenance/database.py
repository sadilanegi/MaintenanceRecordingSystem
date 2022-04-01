from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DB_URL ="postgresql://sumit:root@localhost/maintenance_recording"
engine = create_engine(SQLALCHEMY_DB_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
#SQLALCHEMY_DATABASE_URL = "postgresql://sumit:root@localhost/maintenance_recording"
