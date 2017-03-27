import pymongo

# the single index:
db.restaurants.create_index([("cuisine", pymongo.ASCENDING)])

# the compound index:

first stored by cuisine then within cuisine  by zipcode.
db.restaurants.create_index([
    ("cuisine", pymongo.ASCENDING),
    ("address.zipcode", pymongo.DESCENDING)
])





# General pattern:
 # [ ( <field1>: <type1> ), ... ]