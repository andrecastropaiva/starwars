from app.api_call import api_call
import pymongo
from create_starships_collection import create_starships_collection
from insert_starships import insert_starships_docs
from update_pilots import update_pilots

client = pymongo.MongoClient('mongodb://docker:mongopw@localhost:55000')  # connecting pymongo to MongoDB
db = client['star_wars']  # adding database where we want to connect to

characters = db['characters']  # assigning database characters collection to variable for easier usability
starships = db['starships']  # assigning database starships collection to variable for easier usability


# Main program function, calls all others functions
def app_engine():
    api_call()
    create_starships_collection()
    insert_starships_docs()
    update_pilots()


#  Allows / prevent parts of code from running when the modules are imported.
if __name__ == "__main__":
    app_engine()  # call app_engine() back
