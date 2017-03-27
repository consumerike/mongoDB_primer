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




