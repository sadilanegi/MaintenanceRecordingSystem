from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from ..import schemas,models,database,oauth2
from sqlalchemy.orm import Session
from enum import Enum
import random


router= APIRouter(
    prefix="/maintenance",
    tags=['Maintenance']
)

def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

unique_sequence = uniqueid()

class Month(str, Enum):
    Jan = "January"
    Feb = "February"
    Mar = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "March"
    Aug = "March"
    Sept="September"
    Oct="October"
    Nov="November"
    Dec="December"


## get all aintenance(Order by user id remaining)
@router.get('/',response_model=List[schemas.ShowMaintenanceDetail])
def get_all_maintenance(db:Session = Depends(database.get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    user1 = db.query(models.Maintenance).all()    
    return user1

@router.get('/{user_id}',response_model=List[schemas.ShowMaintenanceDetail])
def get_maintenance(user_id:int,db:Session = Depends(database.get_db)):
    #return db
    user1 = db.query(models.Maintenance).filter(models.Maintenance.user_id == user_id).order_by(models.Maintenance.month).all()
    
    return user1

#get maintenance by month
@router.get('/{months}',response_model=List[schemas.ShowMaintenanceDetail])
def get_maintenance_by_month(months: Month,db:Session = Depends(database.get_db)):
    #return db
    user2 = db.query(models.Maintenance).filter(models.Maintenance.month == months).all()
    return user2    

@router.post('/{months}')
def pay_maintenance(months: Month,db:Session = Depends(database.get_db)):
    monthexist=db.query(models.Maintenance).filter(models.Maintenance.month == months,models.Maintenance.user_id == 5).all()
    if(not monthexist):
        new_user = models.Maintenance(user_id=5,amount=500,transaction_id=next(unique_sequence),month=months)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    else:
        new_user=f"Month {months} Maintenance have been paid"
    return new_user