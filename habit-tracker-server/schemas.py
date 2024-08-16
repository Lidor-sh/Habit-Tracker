from pydantic import BaseModel, EmailStr
from typing import Optional

class BaseSchema(BaseModel):
    class Config:
        model_config = {'from_attributes': True}
        from_attributes = True

class UserSchema(BaseSchema):
    email: EmailStr
    username: str
    password: str
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
