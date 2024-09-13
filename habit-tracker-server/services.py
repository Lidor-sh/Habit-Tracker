import database as db
import models
import schemas
from typing import TYPE_CHECKING
from passlib.context import CryptContext
from pydantic import ValidationError
from fastapi import HTTPException, status, Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import sqlalchemy.orm as orm
from dotenv import load_dotenv
from datetime import timedelta, timezone, datetime
from jwt.exceptions import InvalidTokenError
import jwt
import os
from typing import Annotated


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

load_dotenv(".env")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def add_tables():
    return db.Base.metadata.create_all(bind=db.engine)

def get_db():
    currDB = db.SessionLocal()
    try:
        yield currDB
    finally:
        currDB.close()

async def create_user(user: schemas.UserSchema, db: "Session") -> schemas.UserSchema:
    existing_user = db.query(models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    hashed_password = pwd_context.hash(user.password)
    user = models.User(email=user.email, password=hashed_password, username=user.username, image=user.image)
    db.add(user)
    db.commit()
    db.refresh(user)
    return schemas.UserSchema.model_validate(user)

async def get_user_by_email(email: str, db: "Session") -> schemas.UserSchema:
    user = db.query(models.User).filter_by(email=email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return schemas.UserSchema.model_validate(user)

async def update_user(email: str, user: schemas.UpdateUserSchema, db: "Session") -> schemas.UserSchema:
    existing_user = db.query(models.User).filter_by(email=email).first()
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if user.username:
        existing_user.username = user.username
    if user.password:
        existing_user.password = user.password
    if user.image:
        existing_user.image = user.image
    db.commit()
    db.refresh(existing_user)
    return schemas.UserSchema.model_validate(existing_user)

async def delete_user(email: str, db: "Session"):
    user = db.query(models.User).filter_by(email=email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

async def authenticate_user(email: str, password: str, db: "Session"):
    user = db.query(models.User).filter_by(email=email).first()
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user

async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("JWT_SECRET_KEY"), algorithm=os.getenv("JWT_ALGORITHM"))
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: orm.Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except InvalidTokenError:
        raise credentials_exception
    user = db.query(models.User).filter_by(email=token_data.email).first()
    if user is None:
        raise credentials_exception
    return user