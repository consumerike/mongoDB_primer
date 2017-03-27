from pymongo import MongoClient

client = MongoClient()
db = client.test

#cursor for querying with operators:
# General pattern:
{ <field1>: { <operator1>: <value1> } }

#greater than query
cursor = db.restaurants.find({"grades.score": {"$gt": 30}})

#less than query:
cursor = db.restaurants.find({"grades.score": {"$lt": 10}})

# logical and is executed with a comma separating a list of query conditions:
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})

# logical or is executed with $or:
cursor = db.restaurants.find({"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})







