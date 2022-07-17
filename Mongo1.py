import pymongo
client = pymongo.MongoClient("mongodb+srv://Thanmai1998:Thanmai@thanmai.oczr5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    'name': 'Thanmai',
    'email': 'Thanmai.chandaka@123',
    'surname' : 'Chandaka'
}

db1 = client['mongo1']
collection = db1['test']
collection.insert_one(d)