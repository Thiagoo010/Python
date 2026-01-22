from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import engine
from models.user_models import Base
from dependencies import get_db
from services.user_service import UserService
from schemas.user_schema import UserCreate, UserResponse
from excepts.user_except import UserAlreadyExistsError, UserNotFoundError

app = FastAPI(title="Manejo De Usuarios API")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.post("/usuarios", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.create_user(user)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/usuarios", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()


@app.get("/usuarios/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.get_user_by_id(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
