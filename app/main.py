from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.code_routes import router
from app.routes.auth_routes import auth_router
from app.config import CORS_ALLOW_ORIGINS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS or ["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(auth_router)
