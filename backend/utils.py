# function to get data from google sheets
from pprint import pprint
import gspread
import pandas as pd
from decimal import Decimal

# set up the authentication
gc = gspread.service_account(filename="./keys.json")

def clean(v:str):
    new_value= v.strip().split(" ")[1].split(",")
    return float(new_value[0] + new_value[1])

def clean_two(v:str):
    new_value = v.split(" ")[2].strip(" ").split(",")
    x = new_value[-1]
    y = new_value[0] + x
    return int(y.split(".")[0])


def clean_profit(v:str):
    new_value = v.split(" ")[2].strip("()").split(",")
    x = new_value[-1].split(".")[0]
    y = new_value[0] + x
    return y

def fetch_data_from_gsheets(spreadsheet_name: str, sheet_name:str):
    # locate the spreadsheet
    sh = gc.open(spreadsheet_name)
    worksheet  = sh.worksheet(sheet_name)
    # get all records from the sheet

    # clean the data using pandas
    data = worksheet.get_all_values()
    headers = data.pop(0)

    df = pd.DataFrame(data, columns=headers)
    new_sales = df["  Sales "].apply(clean)
    df.update(new_sales)
    new_cogs = df[" COGS "].apply(clean_two)
    df.update(new_cogs)
    new_series = df[" Profit "].map(clean_profit)
    df.update(new_series)

    records = df.to_dict('records')
    return records