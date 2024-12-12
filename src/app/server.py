import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from sqlalchemy import text

import src.config.globals
from .db import Database
from .exception import validation_exception_handler, app_exception_handler, AppException
from src.middlewares.client import ClientInfoMiddleware
from src.routes import index
from src.utils.commonFunctions import send_response
from src.utils.breeth import ASCII_ART

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await Database.connect()
        yield
    finally:
        await Database.close()

def InitializeServer():
    load_dotenv()

    # Initialize FastAPI app
    app = FastAPI(lifespan=lifespan)

    app.exception_handler(RequestValidationError)(validation_exception_handler)
    app.exception_handler(AppException)(app_exception_handler)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(ClientInfoMiddleware)

    index.init(app)

    @app.get("/check", tags=["Health-check"])
    def read_root(request: Request):
        client_info = request.state.client_info,
        return send_response(SUCCESS, 'App working fine 🤗', client_info)

    @app.get("/", tags=["Home"])
    def read_root():
        return PlainTextResponse(ASCII_ART)

    @app.exception_handler(404)
    async def custom_404_handler(request: Request, exc: HTTPException):
        return send_response(NOT_FOUND, "Sorry the page you are looking for doesn't exist ❌", {}, 'This is not a valid endpoint')

    return app