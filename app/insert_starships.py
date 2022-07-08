from pprint import pprint

import app.api_call
from app.api_call import api_call
from app.update_pilots import starships


# client = pymongo.MongoClient()  # connecting pymongo to docker & db
# db = client['star_wars']  # adding database where we want to connect to


# Insert all starships from API into starships collection in MongoDB
def insert_starships_docs():
    for ship in app.api_call.api_call():  # loops through the created list in the global scope (in main file)
        starships.insert_one(ship)  # updates starships collection with updated data
    list_length = len(app.api_call.api_call())  # counts the number of docs updated
    pprint(f"{list_length} documents inserted successfully in starships collection.")  # prints out the num of docs
    return len(api_call())
