from fastapi import FastAPI, Request
from routes import auth

app = FastAPI()
app.include_router(auth.router)