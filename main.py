from http import HTTPStatus

import uvicorn
from fastapi import FastAPI
from src.api.routers import product_router
from src.api.exception_handlers import internal_server_error_handler

app = FastAPI()

app.include_router(product_router)

app.add_exception_handler(
    HTTPStatus.INTERNAL_SERVER_ERROR,
    internal_server_error_handler
)


if __name__ == "__main__":
    uvicorn.run(app)
