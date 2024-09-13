import datetime as dt
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    PrimaryKeyConstraint,
    Integer,
    LargeBinary,
)
import database as db


class User(db.Base):
    __tablename__ = "users"
    email = Column(String, index=True)
    username = Column(String, index=True)
    password = Column(String)
    image = Column(String)
    __table_args__ = (PrimaryKeyConstraint("email"),)


class Auth(db.Base):
    __tablename__ = "auth"
    email = Column(String, ForeignKey("users.email"), index=True)
    authType = Column(String)
    __table_args__ = (PrimaryKeyConstraint("email", "authType"),)


class Habit(db.Base):
    __tablename__ = "habits"
    name = Column(String, index=True)
    image = Column(String)
    description = Column(String)
    __table_args__ = (PrimaryKeyConstraint("name"),)


class UserHabit(db.Base):
    __tablename__ = "userhabits"
    email = Column(String, ForeignKey("users.email"), index=True)
    habitName = Column(String, ForeignKey("habits.name"), index=True)
    streak = Column(Integer)
    completedDays = Column(LargeBinary)
    __table_args__ = (PrimaryKeyConstraint("email", "habitName"),)
