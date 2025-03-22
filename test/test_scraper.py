import pytest
from web_scraper import movies, web_scrapper

def test_scraper():
    result = web_scraper(movies)
    assert result == list