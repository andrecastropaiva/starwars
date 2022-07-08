import requests

sw_api_url = "https://swapi.dev/api/starships/"
ships_list = []  # list on global scope for easier function access to receive data extracted from API


#  Calling API method
def api_call():
    next_page = sw_api_url  # Gets starship info from the starwars api url(above), assigns it to a variable to loop
    while next_page:  # loops through urls
        response = requests.get(next_page).json()  # gets api response from url into json format
        for ship in response["results"]:  # loops through each ship, filters only the info inside 'results' keyword
            ships_list.append(ship)  # appends the results to the empty list (created above in global scope)
        next_page = response["next"]  # targeting the next keyword (which is the next page url)

