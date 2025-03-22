import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
Api_key = os.getenv("API_KEY_2")


movies = ["Spider", "Ironman", "The Avengers", "Star Wars"]
def web_scrapper(movies):
    # Base url that connect to the server
    url = "https://imdb8.p.rapidapi.com/auto-complete"

    # header to authenticate connection
    header = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': Api_key
    }

    

    responses = []

    # Looping through movies
    for x, i in enumerate(movies):
        querystring = {"q": movies[x]}

    # Query the API and save the result
        try:
            response = requests.request(
                "GET", url, headers=header, params=querystring, timeout=(5, 15))
            data = json.loads(response.text)
        

            formatted_data = json.dumps(data, indent=4)

            data_dict = json.loads(formatted_data)

            responses.append(data_dict["d"])

        
            #print(data_dict)
        except requests.exceptions.Timeout:
            print("The request timed out")

    return responses

a = web_scrapper(movies)
print(a)