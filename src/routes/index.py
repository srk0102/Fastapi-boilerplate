# app/routes/index.py
from fastapi import FastAPI

from .user import UserRouter

# List of all routes
Routes = [
    {"path": "/user", "router": UserRouter, "tag": ["UserRoutes"]},
]

# Init function to register all the routes
def init(app: FastAPI):
    try:
        for route in Routes:
            app.include_router(
                route["router"], prefix=route["path"], tags=route["tag"])
    except Exception as err:
        print(f"Error setting up routes: {err}")
