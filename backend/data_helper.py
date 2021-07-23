from pprint import pprint


def financial_helper(financial) -> dict:
    return {
        "id": str(financial["_id"]),
        "department": financial["Department"],
        "country": financial["Country"],
        "product": financial[" Product "],
        "discount_band": financial[" Discount Band "],
        "units_sold": financial["Units Sold"],
        "manufacturing_price": financial[" Manufacturing Price "],
        "sale_price": financial[" Sale Price "],
        "gross_sales": financial[" Gross Sales "],
        "discounts": financial[" Discounts "],
        "sales": financial["  Sales "],
        "cogs": financial[" COGS "],
        "profit": financial[" Profit "],
        "date": financial["Date"],
        "month_number": financial["Month Number"],
        "month_name": financial[" Month Name "],
        "year": financial[ "Year"]
    }
