from pprint import pprint
import pymongo
import requests

client = pymongo.MongoClient('mongodb://docker:mongopw@localhost:55000')  # connecting pymongo to docker & db
db = client['star_wars']  # adding database where we want to connect to
characters = db['characters']  # gets the characters' collection from star_wars database
starships = db['starships']


def update_pilots():
    ships = starships.find({}, {"_id": 1, "name": 1, "pilots": 1})  # Mongo query to find IDs, names and pilots
    count_updated_docs = 0  # counter to count number of pilot records updated
    for ship in ships:  # loops through the ships variable assigned above

        # Condition to replace only pilots not empty
        if ship["pilots"] is not []:
            # list comprehension creating a pilot names list from pilot urls
            pilot_names = [requests.get(pilot_url).json()["name"] for pilot_url in ship["pilots"]]

            # list comprehension creating a character object IDs list from pilot names
            pilot_ids = [characters.find({"name": names}).next()['_id'] for names in pilot_names]

            # Mongo query: changes the pilots urls (which are arrays) and sets to object ids (which are arrays)
            starships.update_one({'_id': ship['_id']}, {"$set": {"pilots": pilot_ids}})

            # Prints pilot names and corresponding object IDs in python
            for each_pilot in range(len(pilot_names)):  # loops through th range of the pilot names list
                count_updated_docs += 1 # adds 1 at each iteration in the list to counter
                pilots_info = 'Pilot:', pilot_names[each_pilot], 'Object ID:', pilot_ids[each_pilot]
                pprint(pilots_info)
    print(f"{count_updated_docs} pilot documents updated successfully.")
