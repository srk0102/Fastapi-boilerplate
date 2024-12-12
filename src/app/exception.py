from fastapi import HTTPException, Request
from pydantic import ValidationError

import src.config.globals
from src.utils.commonFunctions import send_response

class AppException(HTTPException):
    def __init__(self, message: str, error_type: str = "error", status_code: int = 400):
        super().__init__(status_code=status_code, detail=message)
        self.error_type = error_type

async def app_exception_handler(request: Request, exc: AppException):
    error_detail = {
        "status": exc.error_type,
        "message": exc.detail
    }
    return send_response(
        INTERNAL_SERVER_ERROR,
        message="Something went wrong",
        data=error_detail,
        error="Internal server error",
    )

async def validation_exception_handler(request, exc: ValidationError):
    error_detail = [{"field": e['loc'][1], "message": e['msg']} for e in exc.errors()]
    return send_response(
        UNPROCESSABLE_CONTENT,
        "unable to process the request at this time, Please try again later.",
        error_detail,
        "Request object validation error"
    )