from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from api.endpoints import router

load_dotenv() 
app = FastAPI(title="RL Research", version="1.0.0")
app.include_router(router)