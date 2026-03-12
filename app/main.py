from fastapi import FastAPI
from app.routes.code_routes import router

app = FastAPI()

app.include_router(router)