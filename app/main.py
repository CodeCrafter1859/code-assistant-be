from fastapi import FastAPI
from app.routes.code_routes import router
from app.routes.auth_routes import auth_router

app = FastAPI()

app.include_router(router)
app.include_router(auth_router)