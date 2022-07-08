from app.create_starships_collection import db


# Tests that the starships' collection exists in starwars database
def test_creation_starships():
    assert 'starships' in db.list_collection_names()
