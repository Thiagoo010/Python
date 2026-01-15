from fastapi import FastAPI, HTTPException
from services.user_service import UserService
from schemas.user_schema import UserCreate, UserResponse
from excepts.user_except import UserAlreadyExistsError, UserNotFoundError

app = FastAPI(title="User Management API")

user_service = UserService()


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        return user_service.create_user(user)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/users", response_model=list[UserResponse])
def get_users():
    return user_service.get_all_users()


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    try:
        return user_service.get_user_by_id(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
