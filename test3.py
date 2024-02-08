
import pymongo
client = pymongo.MongoClient("mongodb+srv://Gmgaurav7:Swizzler007@gaurav123.xzfouhd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

collection = client["Inventory"]["Table"]

#d = collection.find({'$or': [{'status': {'$in': ['A', 'P']}},{'qty': 25}]})
#collection.update_many({'item': 'mousepad'} , {'$set':{'item': 'mouse'}})
collection.delete_one({'item': 'canvas'})

d = collection.find({'item': 'canvas'})
for i in d:
    print(i)
