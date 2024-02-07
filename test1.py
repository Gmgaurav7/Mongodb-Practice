import pymongo
client = pymongo.MongoClient("mongodb+srv://Gmgaurav7:Swizzler007@gaurav123.xzfouhd.mongodb.net/?retryWrites=true&w=majority")
db = client.test


collection = client['bank_details']['account_details']
#collection.insert_many([{'Name':'Gaurav','Acc_no.': 101 , 'Balance':1000,'Last 5 Transactions': (20,55,60,98,21)},
#                      {'Name':'Gaurav','Acc_no.': 101 , 'Balance':1000,'Last 5 Transactions': (20,55,60,98,21)},
#                      {'Name':'Gaurav','Acc_no.': 101 , 'Balance':1000,'Last 5 Transactions': (20,55,60,98,21)},
#                      {'Name':'Gaurav','Acc_no.': 101 , 'Balance':1000,'Last 5 Transactions': (20,55,60,98,21)},
#                      {'Name':'Gaurav','Acc_no.': 101 , 'Balance':1000,'Last 5 Transactions': (20,55,60,98,21)},
#                      {'Name':'Gaurav','Acc_no.': 101 , 'Balance':1000,'Last 5 Transactions': (20,55,60,98,21)}])

for i in collection.find():
    print(i)
