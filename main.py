from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# ---------------------------
# Create FastAPI app
# ---------------------------
app = FastAPI(title="Stock Dashboard Backend")

# ---------------------------
# CORS settings (allow React frontend)
# ---------------------------
origins = [
    "http://localhost:3000",  # React app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Data Models
# ---------------------------
class Stock(BaseModel):
    symbol: str
    price: float
    change: float

class Alert(BaseModel):
    symbol: str
    message: str

# ---------------------------
# Sample Data
# ---------------------------
stocks_data = [
    {"symbol": "AAPL", "price": 174.50, "change": +1.2},
    {"symbol": "GOOGL", "price": 134.80, "change": -0.5},
    {"symbol": "TSLA", "price": 289.10, "change": +2.8},
]

alerts_data = [
    {"symbol": "AAPL", "message": "Price crossed above 170"},
    {"symbol": "TSLA", "message": "Price dropped 2% today"},
]

# ---------------------------
# Routes
# ---------------------------
@app.get("/")
def read_root():
    return {"message": "Stock Dashboard Backend is running!"}

@app.get("/stocks", response_model=List[Stock])
def get_stocks():
    return stocks_data

@app.get("/alerts", response_model=List[Alert])
def get_alerts():
    return alerts_data
