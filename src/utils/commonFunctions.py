from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from typing import Any, Optional

from src.config.error import ERRORS

def get_utc_time() -> str:
    """Returns the current timestamp in UTC format with timezone information."""
    return datetime.now(timezone.utc).isoformat()

def send_response(
    status: int,
    message: str,
    data: Optional[Any] = None,
    error: Optional[Any] = None
) -> JSONResponse:
    """
    Sends a structured JSON response.

    Args:
        status (int): HTTP status code.
        message (str): Message to be sent to the client.
        data (dict, optional): Any data to send to the client. Defaults to an empty dictionary.
        error (any, optional): Error information or message. Defaults to None.

    Returns:
        JSONResponse: A JSON response object.
    """

    response_payload = {
        "status": status,
        "message": message,
        "data": data if data is not None else {},
        "error": ERRORS.get(error, error),
        "currentTimeStampInUTC": get_utc_time()
    }

    return JSONResponse(content=response_payload, status_code=status)

