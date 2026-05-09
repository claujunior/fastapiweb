from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from routers.user_router import router

from exceptions.handler import (
    http_exception_handler
)


app = FastAPI()


app.add_exception_handler(
    HTTPException,
    http_exception_handler
)


app.include_router(router)