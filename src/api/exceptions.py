from typing import Any
from http import HTTPStatus

from fastapi import HTTPException


class BaseApplicationException(HTTPException):

    status_code: int = None
    detail: str = "Something went wrong. Please, try again later!"
    headers: dict[str, Any] = None

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail,
            headers=self.headers
        )


class ItemNotFoundError(BaseApplicationException):

    status_code = HTTPStatus.NOT_FOUND
    detail = "Item with given number not found."


class ItemAlreadyExistsError(BaseApplicationException):

    status_code = HTTPStatus.UNPROCESSABLE_ENTITY
    detail = "Item with given number already exists."


class ParsingError(BaseApplicationException):

    def __init__(self, detail: str):
        self.detail = detail
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
