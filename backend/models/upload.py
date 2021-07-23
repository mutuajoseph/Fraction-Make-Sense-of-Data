from typing import Optional

from pydantic import BaseModel, Field

class UploadSchema(BaseModel):
    spreadsheet_name: str = Field(...)
    sheet_name:str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "spreadsheet_name": "Spreadsheet Name",
                "sheet_name": "sheet1"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}