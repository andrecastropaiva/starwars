from app.insert_starships import insert_starships


# checks that the total number of ships inserted into the collection is 36
def test_insert_starships():
    assert insert_starships() == 36
