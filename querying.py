from pymongo import MongoClient

client = MongoClient()
db = client.test

#cursor for querying all documents in collection:

cursor = db.resturants.find()

for document in cursor:
    print(document)

query by top_level field:

cursor = db.resturants.find({"borough": "Long Island"})

for document in cursor:
    print(document)

# for embedded documents use dot notation:
cursor = db.resturants.find("address.zipcode": "98021")


