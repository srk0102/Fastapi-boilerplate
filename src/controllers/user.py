from fastapi import Request, Depends, Query
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import Optional

import src.config.globals
from src.app.exception import AppException
from src.app.db import Database

from src.models.user import User
from src.validations.userValidation import UserCreate, UserResponse, UserUpdate
from src.utils.model_utils import str_to_objectid
from src.utils.commonFunctions import send_response


async def create_user(request: Request, user: UserCreate, db:AsyncIOMotorDatabase = Depends(Database.get_db)):
    try:
        existing_user = await db["users"].find_one({"email": user.email})
        if existing_user:
            return send_response(200, "User with this email already exists", {
                "user_data": UserResponse.from_mongo(existing_user).dict()
            })
        db_user = User(**user.dict())
        result = await db["users"].insert_one(db_user.dict(by_alias=True))
        db_user.id = str(result.inserted_id)
        return send_response(CREATED, "User created successfully", jsonable_encoder(UserResponse.from_mongo(db_user)))
    except Exception as e:
        raise AppException(
            message="An unexpected error occurred: " + str(e),
            error_type="INTERNAL_ERROR",
            status_code=500,
        )

async def read_users_by_id(id: Optional[str] = Query(None, description="User ID to search"), db=Depends(Database.get_db)):
    try:
        if id:
            # Search for the user by id
            user = await db["users"].find_one({"_id": str_to_objectid(id)})
            if user:
                return send_response(SUCCESS, "User fetched successfully", jsonable_encoder(UserResponse.from_mongo(user)))
            return send_response(NOT_FOUND, "User not found")
        else:
            # Fetch all users
            # You can set a limit here
            users = await db["users"].find().to_list(length=100)
            if users:
                return send_response(SUCCESS, 'Users fetched successfully', [jsonable_encoder(UserResponse.from_mongo(user)) for user in users])
            return send_response(NOT_FOUND, 'No users found')

    except Exception as e:
        raise AppException(
            message="An unexpected error occurred: " + str(e),
            error_type="INTERNAL_ERROR",
            status_code=500,
        )

async def update_users_by_id(user_id: str, user_update: UserUpdate, db=Depends(Database.get_db)):
    try:
        # Fetch the user from the database by id
        user = await db["users"].find_one({"_id": str_to_objectid(user_id)})
        if not user:
            return send_response(NOT_FOUND, "Requested user not found to update the details", {}, "user not found in database")

        # Update user data
        # Only update fields provided
        update_data = user_update.dict(exclude_unset=True)
        await db["users"].update_one({"_id": str_to_objectid(user_id)}, {"$set": update_data})

        # Fetch the updated user
        updated_user = await db["users"].find_one({"_id": str_to_objectid(user_id)})
        return send_response(SUCCESS, "User updated successfully", jsonable_encoder(UserResponse.from_mongo(updated_user)))

    except Exception as e:
        raise AppException(
            message="An unexpected error occurred: " + str(e),
            error_type="INTERNAL_ERROR",
            status_code=500,
        )
