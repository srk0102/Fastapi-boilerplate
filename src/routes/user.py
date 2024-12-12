# src/routes/user_routes.py
from fastapi import APIRouter

from src.controllers.user import create_user, read_users_by_id, update_users_by_id

UserRouter = APIRouter()

# Route to create a new user
UserRouter.post("/users/")(create_user)
UserRouter.get("/users/")(read_users_by_id)
UserRouter.put("/users/")(update_users_by_id)
