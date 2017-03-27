from pymongo import MongoClient

client = MongoClient()
db = client.test


# remove_first_match:

result = db.restaurants.delete_one({"borough": "Manhattan"})

# remove all matches:
result = db.restaurants.delete_many({"borough": "Manhattan"})

#report of deletions:
result.deleted_count


#Remove entire collection/the collection itself remains:
result = db.restaurants.delete_many({})

# Drop the entire collection:
db.restaurants.drop()

