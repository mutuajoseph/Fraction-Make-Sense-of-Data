from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import function to get datafrom gsheets
from utils import fetch_data_from_gsheets

# import the route
from routes.financial_route import router as FinanceDataRouter

app = FastAPI(
    title="Make Data Sensible",
    description="A simple API that lets a user upload data and make sense of it, across an organization",
    version="1.0.0"
)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return {"message": "Welcome to Fraction assessment API"}

app.include_router(FinanceDataRouter, tags=["Financial Data"], prefix="/sample-data")


# data_records = upload_data("Engineering Exercise Data - Fraction", "HR Data")

