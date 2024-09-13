from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
import schemas
import sqlalchemy.orm as orm
import services
from datetime import timedelta
import os
import dotenv

app = FastAPI()
dotenv.load_dotenv(".env")


@app.post("/api/users/", response_model=schemas.UserSchema)
async def create_user(
    user: schemas.UserSchema, db: orm.Session = Depends(services.get_db)
):
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
async def update_user(
    email: str,
    user: schemas.UpdateUserSchema,
    db: orm.Session = Depends(services.get_db),
):
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
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: orm.Session = Depends(services.get_db),
):
    try:
        user = await services.authenticate_user(
            email=form_data.username, password=form_data.password, db=db
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or passwßord",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(
            minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))
        )
        access_token = await services.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return schemas.TokenSchema(access_token=access_token, token_type="bearer")
    except HTTPException as err:
        raise err


@app.get("/api/user/me", response_model=schemas.UserSchema)
async def get_me(
    current_user: Annotated[schemas.UserSchema, Depends(services.get_current_user)]
):
    print("Main:getdurrrent")
    return current_user
