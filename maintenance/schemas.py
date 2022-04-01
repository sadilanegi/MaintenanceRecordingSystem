from pydantic import BaseModel,EmailStr
from datetime import datetime,timezone
from typing import List, Optional




class ShowUser(BaseModel):          
    name:str
    roomno:int
    email :EmailStr
    
    class Config():
        orm_mode=True

class AdminUser(ShowUser):          
    is_admin=bool

class SuperUser(ShowUser):          
    is_admin=bool

class User(ShowUser):
    password :str
    # class Config():
    #     orm_mode=True


class Maintenance(BaseModel):          
    month = str      
    class Config():
        orm_mode=True
   
class ShowMaintenanceDetail(BaseModel):
    users_id = int
