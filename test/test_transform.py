import pytest
from web_scraper import movies, web_scrapper
from data_transform import result, clean_data
import pandas as pd

def test_transfrom():
    output = result(movies)
    assert output == pandas.core.frame.DataFrame