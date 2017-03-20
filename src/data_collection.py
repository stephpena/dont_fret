import numpy as np
import pandas as pd
import pymongo
import requests
from bs4 import BeautifulSoup
import time
import json
from selenium import webdriver
import sys
import time
import re
from unidecode import unidecode



def get_full_url_html(base_url="http://equipboard.com", url_ext="/role/guitarists", num_range=120):
    """
    Webscrapes to retrieve initial html of guitarists on the Equipboard website.
    Scrolls down through the infinite scrolls and then retrieves the html.

    Parameters
    ----------
    num_range: int
        number of times to scroll down the webpage
    base_url: str
        main webpage
    url_ext: str
        extension for the specific category

    Returns
    -------
    soup: BeautifulSoup object
        BeautifulSoup object with provided url's html

    Future Work
    -----------
    - Currently defaulted to pull guitarists only. May eventually want to produce similar recommendations for other musicians
    """

    driver.get(base_url+url_ext)
    for i in range(0,num_range):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(6)
    html_data = driver.page_source
    soup = BeautifulSoup(html_data, 'html.parser')
    return soup
