import pymongo

cursor = db.restaurants.find().sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.DESCENDING)
])

for document in cursor:
    print(document)

