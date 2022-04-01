from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean,DateTime
from .database import Base
from sqlalchemy.orm import relationship

            
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    roomno = Column(Integer)
    password = Column(String)
    is_admin = Column(Boolean,default=False)
    is_suadmin = Column(Boolean,default=False)
    created_at = Column(DateTime,default=datetime.utcnow)
    updated_at = Column(DateTime,default=datetime.utcnow)   

    member = relationship('Maintenance', back_populates="maintain")


class Maintenance(Base):
    __tablename__ = 'maintenance'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    month = Column(String)
    amount = Column(Integer)
    transaction_id = Column(String(100))

    maintain = relationship("User", back_populates="member")    