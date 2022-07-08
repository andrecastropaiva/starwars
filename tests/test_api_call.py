import requests


# Tests validity of api requests
def test_validity_api_requests():
    good_requests = requests.get("https://swapi.dev/api/starships/") or requests.get("https://swapi.dev/api/")
    bad_requests = requests.get("https://swapi.dev/api/aaa") or requests.get("https://swapi.dev/aaa")
    assert good_requests.status_code == 200  # if gets HTTP response 200 means ok aka good request
    assert bad_requests.status_code == 404  # if gets HTTP response 404 means bad request
