# updates first document with name of 'Juni'

# The $set operator updates  the cuisine field
# $currentDate operator to update the lastModified field with the current date

result = db.restaurants.update_one(
    {"name": "Juni"},
    {
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)

# result.matched_count: stats about matching documents
# result.modified_count: count of the mods made

# update_many updates all documents that match the query:
result = db.restaurants.update_many(
    {"address.zipcode": "10016", "cuisine": "Other"},
    {
        "$set": {"cuisine": "Category To Be Determined"},
        "$currentDate": {"lastModified": True}
    }
)

# Replacing a document: replaces the first argument, or the restaruant
# with the id starting with 4170 with the object that starts with "name" and ends with
# zipcode
result = db.restaurants.replace_one(
    {"restaurant_id": "41704620"},
    {
        "name": "Vella 2",
        "address": {
            "coord": [-73.9557413, 40.7720266],
            "building": "1480",
            "street": "2 Avenue",
            "zipcode": "10075"
        }
    }
)