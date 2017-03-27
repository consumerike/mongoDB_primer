from pymongo import MongoClient

client = MongoClient()
db = client.test

# $ = stages, e.g. $group is group stage.
# $group by a specified key in this case borough using the _id field. The path is $borough, which 
# which is the key preceded by a '$', accumulators like "$sum" can be used to 
# perform calculations for each group.

cursor = db.restaurants.aggregate(
    [
        {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
    ]
)

