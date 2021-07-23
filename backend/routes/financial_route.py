from pprint import pprint
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from db_config import retrieve_financial_data, group_data
from pprint import pprint

# import the model
from models.upload import UploadSchema

# import the db collection
from db_config import fraction_collection

# import function to get datafrom gsheets
from utils import fetch_data_from_gsheets

router = APIRouter()

@router.post("/upload-data", response_description="Data uploaded to db")
async def upload_data(sample_data: UploadSchema = Body(...)):
    try: 
        sample_data = jsonable_encoder(sample_data)
        # pprint(sample_data)

        # # get sample data 
        spreadsheet_data = fetch_data_from_gsheets(sample_data["spreadsheet_name"], sample_data["sheet_name"])
        # pprint(spreadsheet_data)

        # # get collection to insert data 
        records = fraction_collection

        # insert data to database
        records.insert_many(spreadsheet_data)
        return {"message": "Data uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500 , detail=f"{e}")

@router.get("/", response_description="Financial data retrieved")
async def get_data():
    try: 
        financial_data = await retrieve_financial_data()
        return JSONResponse(financial_data)
    except Exception as e:
        pprint(e)
        raise HTTPException(status_code=500, detail=f"{e}")

@router.get("/sales", response_description="Grouped data received")
async def get_grouped_data():
    try:
        
        fetch_data = await group_data()
        products = []
        total_sales = []
        total_cogs = []

        for each in fetch_data:
            products.append(each["_id"])
            total_sales.append(each["total_sales"])   
            total_cogs.append(each["total_cogs"])     

        grouped_data = {
            "labels": products,
            "total_sales": total_sales,
            "total_cogs": total_cogs
        }

        return grouped_data
    except Exception as e:
        pprint(e)