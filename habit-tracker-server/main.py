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
    except HTTPException as e:
        raise e