import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv
from model import engine, Movie, session

load_dotenv()
Api_key = os.getenv("API_KEY_1")


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


def result(movies):
    title = []
    #movie_lenght = []
    movie_id = []
    image_url = []
    series_type = []
    rank = []
    casts = []
    year = []

    response = web_scrapper(movies)

    for i in range(len(movies)):
        try:
            for movie in response[i]:
                movie_id.append(movie["id"])
                title.append(movie["l"])
                image_url.append(movie["i"]["imageUrl"])
                series_type.append(movie["qid"])
                rank.append(movie["rank"])
                casts.append(movie["s"])
                year.append(movie["y"])
        except:
            pass
    try:
        df = pd.DataFrame([movie_id, title, image_url, series_type, rank, casts, year]).T
        df.columns = ["movie_id", "title", "image_url", "series_type", "rank", "casts", "year"]
    except ValueError as e:
        print("Num of header does not match num of columns")
        
    return df

def clean_data():
    df = result(movies)
    df.isnull().sum()
    df.fillna("")
    #df = df[df.duplicated(keep="first")]
    return df

data = clean_data()


def load_data():
    for i, r in data.iterrows():
        movie = Movie(movie_id = r["movie_id"],
                      title = r["title"],
                    image_url = r["image_url"],
                    serie_type = r["series_type"],
                    rank = r["rank"],
                    casts = r["casts"],
                    year = r["year"])
    
    return session.add(movie), session.commit()

load_data()

