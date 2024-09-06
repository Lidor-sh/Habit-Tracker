import database as db
import models
import schemas
from typing import TYPE_CHECKING
from passlib.context import CryptContext
from pydantic import ValidationError
from fastapi import HTTPException, status

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

pwd_context = CryptContext()

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
    
    user = models.User(**user.dict())
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
