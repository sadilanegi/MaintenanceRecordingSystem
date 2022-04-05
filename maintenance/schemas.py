import email
from pydantic import BaseModel,EmailStr
from datetime import datetime,timezone
from typing import List, Optional

class User(BaseModel):
    pass
    
class GetUser(User):
    name:str
    email :EmailStr
    class Config():
        orm_mode=True

class SuperUser(GetUser):
    password:str

class CreateUser(SuperUser):
    roomno:int

class ShowUser(GetUser):
    id:int
    roomno:int
    is_admin:bool
    class Config():
        orm_mode=True

class UpdateUser(BaseModel):
    name:Optional[str]=None
    roomno:Optional[int]=None
    email :Optional[EmailStr]=None
    class Config():
        orm_mode=True

class Maintenance(BaseModel):    
    pass      
    # month = str      
    class Config():
        orm_mode=True
   
class ShowMaintenanceDetail(Maintenance):
    user_id: int
    amount: int
    month: str
    transaction_id:str
    maintain : ShowUser

class Login(BaseModel):
    username:EmailStr
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

