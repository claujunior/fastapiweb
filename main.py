from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from routers.user_router import router
from fastapi.middleware.cors import CORSMiddleware
from exceptions.handler import (
    http_exception_handler
)


app = FastAPI()


app.add_exception_handler(
    HTTPException,
    http_exception_handler
)


app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  
    allow_methods=["*"],
    allow_headers=["*"],
)