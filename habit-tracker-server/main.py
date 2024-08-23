from fastapi import FastAPI, Depends, HTTPException
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
