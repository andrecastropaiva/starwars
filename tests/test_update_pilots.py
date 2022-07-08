from app.update_pilots import starships, characters  # imports starships and characters collections


# Checks if pilots urls were changed to the respective object IDs
def test_update_pilots():
    assert isinstance(starships["pilots"], type(characters["_id"]))  # compares if both types match
