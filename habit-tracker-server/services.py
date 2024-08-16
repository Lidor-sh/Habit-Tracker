import database as db
import models
import schemas
from typing import TYPE_CHECKING
from pydantic import ValidationError
from fastapi import HTTPException, status

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

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
