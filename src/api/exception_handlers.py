from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse


async def internal_server_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"detail": "Something went wrong. Please, try again later!"}
    )
