from fastapi import FastAPI
from apps.users.routers import router

app = FastAPI()

app.include_router(router)


