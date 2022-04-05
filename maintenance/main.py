from fastapi import  FastAPI

from maintenance.routers import authentiation
from . import models
from .database import engine
from .routers import maintenance,user,authentiation

description = """
Maintenance Recording App helps you manage your maintenance in one place. 🚀

## User
You will be able to:

* **Create Super users,Admin users and End Users**.
* **Get Users Data**.


## Maintenance

You will be able to:

* **Pay Maintenance**.
* **Get Maintenance Record**.
"""
app=FastAPI(
    docs_url="/Maintenance",
    title="Maintenance Recording System",
    description=description
)

models.Base.metadata.create_all(engine)
app.include_router(authentiation.router)
app.include_router(user.router)
app.include_router(maintenance.router)

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
    


##########################################################################################################
# @app.post('/blog',status_code=status.HTTP_201_CREATED)
# def create(request:schemas.Blog,db:Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
# def delete(id,db:Session = Depends(get_db)):
#     # no need of storing value in variable as we dont have to display data in delete
#     #blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
# def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#     blog.update(request.dict())
#     # blog.title = request.title
#     # blog.body = request.body      
#     db.commit()
#     return 'Updated Successfully'

# @app.get('/blog',response_model=List[schemas.ShowBlog])
# def all(db:Session = Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
# def show(id, response:Response, db:Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return{'detail':f"Blog with id {id} is not available"}
#     return blog
######################################################################################################
# pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")
# ##############################################!!!!Super User!!!!!########################################################

# #Create Super User
# @app.post('/user/super',tags=['Users'])
# def create_superuser(request:schemas.User,db:Session = Depends(get_db)): #,is_admin:Optional[bool]=True
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(is_suadmin=True,name=request.name,roomno=request.roomno,email = request.email,password=hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# #Show Super Users
# @app.get('/user/super',response_model=List[schemas.SuperUser],tags=['Users'])
# def show_super(db:Session = Depends(get_db)):
#     user=db.query(models.User).filter(models.User.is_admin == True).all()
#     return user


# ##############################################!!!Admin User!!!##################################################
# @app.post('/user/admin',tags=['Users'])
# def create_adminuser(request:schemas.User,db:Session = Depends(get_db)): #,is_admin:Optional[bool]=True
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(is_admin=True,name=request.name,roomno=request.roomno,email = request.email,password=hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/admin',response_model=List[schemas.AdminUser],tags=['Users'])
# def show_admin(db:Session = Depends(get_db)):
#     user=db.query(models.User).filter(models.User.is_admin == True).all()
#     return user

# ##################################################!!!!!!Users!!!!!##############################################
# @app.post('/user',tags=['Users'])
# def create_user(request:schemas.User,db:Session = Depends(get_db)):
#     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.User(name=request.name,roomno=request.roomno,email = request.email,password=hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# # getuser detail by name 
# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['Users'])
# def get_user(id:int,db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     return user

# @app.get('/user',response_model=List[schemas.ShowUser],tags=['Users'])
# def all_user(db:Session = Depends(get_db)): 
#     user=db.query(models.User).filter(models.User.is_admin == False,models.User.is_admin == False).all()
#     return user
#########################################!!!!!!Maintenance!!!!!##################################################
#tags: List[str] = []

# @app.post('/maintenance/{months}',tags=['Maintenance'])
# def pay_maintenance(months: Month,db:Session = Depends(get_db)):
#     monthexist=db.query(models.Maintenance).filter(models.Maintenance.month == months,models.Maintenance.user_id == 1).all()
#     if(not monthexist):
#         new_user = models.Maintenance(user_id=1,amount=500,transaction_id=next(unique_sequence),month=months)
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#     else:
#         new_user=f"Month {months} Maintenance have been paid"

#     return new_user


# get maintenance by userid
# @app.get('/maintenance/{user_id}',response_model=List[schemas.ShowMaintenanceDetail],tags=['Maintenance'])
# def get_maintenance(user_id:int,db:Session = Depends(get_db)):
#     #return db
#     user1 = db.query(models.Maintenance).filter(models.Maintenance.user_id == user_id).order_by(models.Maintenance.month).all()
    
#     return user1
    

# .filter(models.Maintenance.user_id == user_id
# user=db.query(models.User).filter(models.User.is_admin,models.User.is_admin == False).all()


# #get maintenance by month
# @app.get('/maintenance/{months}',response_model=List[schemas.ShowMaintenanceDetail],tags=['Maintenance'])
# def get_maintenance_by_month(months: Month,db:Session = Depends(get_db)):
#     #return db
#     user2 = db.query(models.Maintenance).filter(models.Maintenance.month == months).all()
#     return user2    

# get all maintenance(Order by user id remaining)
# @app.get('/maintenance/',response_model=List[schemas.ShowMaintenanceDetail],tags=['Maintenance'])
# def get_all_maintenance(db:Session = Depends(get_db)):
#     #return db
#     user1 = db.query(models.Maintenance).all()
    
#     return user1
    