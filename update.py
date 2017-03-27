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