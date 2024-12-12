from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from bson import ObjectId

from src.utils.model_utils import PyObjectId

class User(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    email: EmailStr
    password_hash: str
    team_name: Optional[str] = None
    user_token: Optional[str] = None
    dashboards: Optional[List[str]] = None
    status: str = "active"
    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        from_attributes = True
