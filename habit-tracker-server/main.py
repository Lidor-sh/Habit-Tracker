from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import schemas
import sqlalchemy.orm as orm
import services

app = FastAPI() 

@app.post("/api/users/", response_model=schemas.UserSchema)
async def create_user(user: schemas.UserSchema, db: orm.Session = Depends(services.get_db)):
    try:
        return await services.create_user(user=user, db=db)
    except HTTPException as err:
        raise err
    
@app.get("/api/users/{email}", response_model=schemas.UserSchema)
async def get_user(email: str, db: orm.Session = Depends(services.get_db)):
    try:
        return await services.get_user_by_email(email=email, db=db)
    except HTTPException as err:
        raise err
    
@app.put("/api/users/{email}", response_model=schemas.UserSchema)
async def update_user(email: str, user: schemas.UpdateUserSchema, db: orm.Session = Depends(services.get_db)):
    try:
        return await services.update_user(email=email, user=user, db=db)
    except HTTPException as err:
        raise err
    
@app.delete("/api/users/{email}")
async def delete_user(email: str, db: orm.Session = Depends(services.get_db)):
    try:
        return await services.delete_user(email=email, db=db)
    except HTTPException as err:
        raise err
    
@app.post("/api/login", response_model=schemas.TokenSchema)
async def login(email:str, password:str, db: orm.Session = Depends(services.get_db)):
    try:
       user = await services.authenticate_user(email=email, password=password, db=db)
       if not user:
           raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Incorrect email or password",
               headers={"WWW-Authenticate": "Bearer"},
           )
    except HTTPException as err:
        raise err