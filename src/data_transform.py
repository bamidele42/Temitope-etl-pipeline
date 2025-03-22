import requests
import json
import pandas as pd
from web_scraper import movies, web_scrapper

def result(movies):
    title = []
    movie_id = []
    poster_url = []
    movie_type = []
    movie_rank = []
    casts = []
    year = []

    response = web_scrapper(movies)

    for i in range(len(movies)):
        try:
            for movie in response[i]:
                movie_id.append(movie["id"])
                title.append(movie["l"])
                poster_url.append(movie["i"]["imageUrl"])
                movie_type.append(movie["qid"])
                movie_rank.append(movie["rank"])
                casts.append(movie["s"])
                year.append(movie["y"])
        except:
            pass
    try:
        df = pd.DataFrame([movie_id, title, poster_url, movie_type, movie_rank, casts, year]).T
        df.columns = ["movie_id", "title", "poster_url", "movie_type", "movie_rank", "casts", "year"]
    except ValueError as e:
        print("Num of header does not match num of columns")
        
    return df


def clean_data():
    df = result(movies)
    df.fillna("")
    #df = df[df.duplicated(keep="first")]
    print(df.head())
    return df

data = clean_data()
print(data)