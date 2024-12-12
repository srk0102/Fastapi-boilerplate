from bson import ObjectId

class PyObjectId(ObjectId):
    """Custom ObjectId class to handle BSON ObjectId in Pydantic models."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field: str, field_info: dict):
        return {"type": "string", "description": "MongoDB ObjectId"}


def str_to_objectid(id: str) -> ObjectId:
    return ObjectId(id)