from pprint import pprint
import motor.motor_asyncio

from data_helper import financial_helper

MONGO_DB_URI = "mongodb+srv://wamzy:Jose.2018@cluster0.asw7f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)

database = client.fraction_data

fraction_collection = database.get_collection("financial_data")


async def retrieve_financial_data():
    new_data = []
    async for single_data in fraction_collection.find():
        new_data.append(financial_helper(single_data))

    return new_data

async def group_data():
    new_data = []
    async for single_data in fraction_collection.aggregate(
        [{
            "$group" : {
                "_id": "$ Product ",
                "total_sales": {"$sum": "$  Sales "},
                "total_cogs":{"$sum": "$ COGS "}
            }
        }]
    ):
        new_data.append(single_data)

    return new_data   

