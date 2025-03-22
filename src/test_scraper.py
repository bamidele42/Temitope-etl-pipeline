import pytest
from web_scraper import movies, web_scrapper


def test_scraper():
    result = wb.web_scrapper(wb.movies)
    assert result == type(list)