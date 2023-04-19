from http import HTTPStatus

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import product_router
from src.api.exception_handlers import internal_server_error_handler

app = FastAPI()

app.include_router(product_router)

app.add_exception_handler(
    HTTPStatus.INTERNAL_SERVER_ERROR,
    internal_server_error_handler
)

origins = ["*"]  # specify your origins here, for example ["http://mysite.ru"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=[
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin"
    ]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
