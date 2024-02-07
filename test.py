import pymongo
client = pymongo.MongoClient("mongodb+srv://Gmgaurav7:Swizzler007@gaurav123.xzfouhd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {'Name': 'Vaibhav', 'email':'vaibhav@gmail.com','Subject':['Accounts','Economics','Maths','English','Physical Education']}

database = client['Test1']
collection = database['Gaurav']
collection.insert_one(data)