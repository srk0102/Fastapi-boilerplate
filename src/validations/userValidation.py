from pydantic import EmailStr, UUID4
from typing import List, Optional
from src.utils.validation_utils import BaseModel
from bson import ObjectId


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password_hash: str
    team_name: Optional[str] = None
    dashboards: Optional[List[str]] = None

    class Config:
        extra = "forbid"

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    email: str
    team_name: Optional[str] = None
    dashboards: Optional[List[str]] = None
    status: str

    class Config:
        from_attributes = True

    @classmethod
    def from_mongo(cls, data: dict):
        # Convert MongoDB _id (ObjectId) to string
        if "_id" in data:
            data["id"] = str(data["_id"])  # MongoDB ObjectId to string
            del data["_id"]  # Remove the _id field
        return cls(**data)

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    team_name: Optional[str] = None
    dashboards: Optional[List[str]] = None
