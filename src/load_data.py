
from model import engine, Movie, session
from web_scraper import web_scrapper, result, clean_data

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