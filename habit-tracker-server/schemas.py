from pydantic import BaseModel, EmailStr
from typing import Optional

class BaseSchema(BaseModel):
    class Config:
        model_config = {'from_attributes': True}
        from_attributes = True

class TokenSchema(BaseSchema):
    access_token: str
    token_type: str

class TokenData(BaseSchema):
    email: EmailStr

class UserSchema(BaseSchema):
    email: EmailStr
    username: str
    password: str
    image: Optional[str] = None

class UpdateUserSchema(BaseSchema):
    username: Optional[str] = None
    password: Optional[str] = None
    image: Optional[str] = None

class AuthSchema(BaseSchema):
    email: EmailStr
    authType: str

class HabitSceme(BaseSchema):
    name: str
    image: Optional[str] = None
    description: Optional[str] = None

class UserHabitSchema(BaseSchema):
    email: EmailStr
    name: str
    streak: int
    completedDays: bytes
