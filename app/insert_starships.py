from pprint import pprint
import pymongo
from app.api_call import ships_list
from app.update_pilots import starships

#client = pymongo.MongoClient("mongodb://docker:mongopw@localhost:55000/")  # connecting pymongo to docker & db
#db = client['star_wars']  # adding database where we want to connect to


# Insert all starships from API into starships collection in MongoDB
def insert_starships():
    for ship in ships_list:  # loops through the created list in the global scope (in main file)
        starships.insert_one(ship)  # updates starships collection with updated data
    list_length = len(ships_list)  # counts the number of docs updated
    pprint(f"{list_length} documents inserted successfully in starships collection.")  # prints out the num of docs
