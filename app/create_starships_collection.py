import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://docker:mongopw@localhost:55000/")  # connecting pymongo to docker & db
db = client['star_wars']


# Drops collection first and creates collection
def create_starships_collection():
    db.starships.drop()
    db.create_collection('starships')
    pprint("Collection created.")
