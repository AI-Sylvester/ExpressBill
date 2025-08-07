from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import itemroutes, orderroutes
from db import test_db_connections

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(itemroutes.router)
app.include_router(orderroutes.router)

# Startup hook
@app.on_event("startup")
async def startup_event():
    print("🔄 Testing DB connections...")
    test_db_connections()
