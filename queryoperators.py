from pymongo import MongoClient

client = MongoClient()
db = client.test

#cursor for querying with operators:
{ <field1>: { <operator1>: <value1> } }
cursor = db.restaurants.find({"grades.score": {"$gt": 30}})

# General pattern:

