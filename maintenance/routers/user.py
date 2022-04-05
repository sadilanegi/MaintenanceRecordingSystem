import bcrypt
from fastapi import APIRouter,Depends,status,Response,HTTPException
from pydantic import EmailStr
from typing import List
from ..import schemas,models,database
from ..hashing import Hash
from sqlalchemy.orm import Session


router= APIRouter(
    prefix="/user",
    tags=['Users']
)


##############################################!!!!Super User!!!!!########################################################

#Create Super User
@router.post('/super',status_code=status.HTTP_201_CREATED)
def create_superuser(response: Response,request:schemas.SuperUser,db:Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        new_user = models.User(is_suadmin=True,name=request.name,email = request.email,password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        return 'User With Same Email Already Exist'


#Show Super Users
@router.get('/super',response_model=List[schemas.GetUser])
def show_super(db:Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.is_suadmin == True).all()
    return user

##############################################!!!!Super User!!!!!########################################################

#Create Admin User
@router.post('/admin',status_code=status.HTTP_201_CREATED)
def create_adminuser(request:schemas.CreateUser,db:Session = Depends(database.get_db)): 
    user=db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        new_user = models.User(is_admin=True,name=request.name,roomno=request.roomno,email = request.email,password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        return 'User With Same Email Already Exist'

#Create User 
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.CreateUser,db:Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        new_user = models.User(name=request.name,roomno=request.roomno,email = request.email,password=Hash.bcrypt(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        return 'User With Same Email Already Exist'


# getuser detail by email 
@router.get('/{email}',response_model=schemas.ShowUser)
def get_user_by_mail(email:EmailStr,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user

# Show User (Admin + User)
@router.get('/',response_model=List[schemas.ShowUser],tags=['Users'])
def get_all_user(db:Session = Depends(database.get_db)): 
    user=db.query(models.User).filter(models.User.is_suadmin == False).all()
    return user

# Show AdminUser
@router.get('/admin',response_model=List[schemas.ShowUser],tags=['Users'])
def admin_user(db:Session = Depends(database.get_db)): 
    user=db.query(models.User).filter(models.User.is_admin == True).all()
    return user

#Update User to Admin
@router.put('/admin/{email}')    #patch is also there
def user_to_admin(email:EmailStr,request:schemas.UpdateUser,db:Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == email)
    # return user
    if not user:
        return 'User With Email Doesnt Exist'
    db.query(models.User).filter(models.User.email == email).update(models.User.is_admin == True)
    db.commit()
    return 'Updated To admin'


#Update User
@router.put('/{email}')    #patch is also there
def update(email:EmailStr,request:schemas.UpdateUser,db:Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == email)
    # return user
    if not user:
        return 'User With Email Doesnt Exist'
    db.query(models.User).filter(models.User.email == email).update(request.dict())
    db.commit()
    return 'Updated'


@router.delete('/{id}')
def delete(id:int,response: Response,db:Session = Depends(database.get_db)):
    # no need of storing value in variable as we dont have to display data in delete
    #blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    user=db.query(models.User).filter(models.User.id == id)
    if not user:
        return 'User Doesnt Exist'
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



# #Show Super Users
# @router.get('/super',response_model=List[schemas.SuperUser])
# def show_super(db:Session = Depends(database.get_db)):
#     user=db.query(models.User).filter(models.User.is_admin == True).all()
#     return user


# ##############################################!!!Admin User!!!##################################################
# @router.post('/admin')
# def create_adminuser(request:schemas.User,db:Session = Depends(database.get_db)): #,is_admin:Optional[bool]=True
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(is_admin=True,name=request.name,roomno=request.roomno,email = request.email,password=hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user



# ##################################################!!!!!!Users!!!!!##############################################
# @router.post('/')
# def create_user(request:schemas.User,db:Session = Depends(database.get_db)):
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(name=request.name,roomno=request.roomno,email = request.email,password=hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# # getuser detail by name 
# @router.get('/{id}',response_model=schemas.ShowUser)
# def get_user(id:int,db:Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     return user

