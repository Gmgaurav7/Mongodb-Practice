
import pymongo
client = pymongo.MongoClient("mongodb+srv://Gmgaurav7:Swizzler007@gaurav123.xzfouhd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

collection = client["Inventory"]["Table"]

d = collection.find({'$or': [{'status': {'$in': ['A', 'P']}},{'qty': 25}]})
for i in d:
    print(i)
