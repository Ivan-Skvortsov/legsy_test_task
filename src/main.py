from http import HTTPStatus

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import product_router
from src.api.exception_handlers import internal_server_error_handler
from src.configs.log import configure_logging


def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI()

    app.include_router(product_router)

    app.add_exception_handler(
        HTTPStatus.INTERNAL_SERVER_ERROR,
        internal_server_error_handler
    )

    # specify your origins here, for example ["http://mysite.ru"]
    origins = ["*"]

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
    return app
