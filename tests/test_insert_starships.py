from app.insert_starships import insert_starships_docs


# checks that the total number of ships inserted into the collection is 36
def test_insert_starships_docs():
    assert insert_starships_docs() == 36
