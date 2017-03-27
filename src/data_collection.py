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


class EquipboardScrapper(object):

      def __init__(self,):
          self.model = model

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
        driver = webdriver.Firefox()
        driver.get(base_url+url_ext)
        for i in range(0,num_range):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(6)
        html_data = driver.page_source
        soup = BeautifulSoup(html_data, 'html.parser')
        return soup

    def html_to_lists(html, tag, att, base_tag='li', base_att='class', base_att_value='span2'):
        all_data = html.find_all(base_tag, {base_att : base_att_value})
        tag_data = []
        for tags in all_data:
            tag_data.append((tags.find(tag)[att].encode('utf-8')))
        return tag_data

    def html_to_lists_alt(html, base_tag='a', base_att='itemprop', base_att_value='memberOf'):
        all_data = html.find_all(base_tag, {base_att : base_att_value})
        tag_data = []
        for tags in all_data:
            tag_data.append((tags.getText().encode('utf-8').strip()))
        return tag_data

    def html_to_lists_alt2(html):
        finder = re.compile('.category/*')
        all_data = [x for x in html.find_all('a', {'href' : re.compile('/category/*')})]
        tag_data = []
        for tags in all_data:
            tag_data.append((tags.getText().encode('utf-8')))
        return tag_data

    def get_equipment_html(equip_type, url):
        equip_type_url = '/#' + equip_type
        driver = webdriver.Firefox()
        driver.get(base_url + url + equip_type_url)
        time.sleep(2)
        html2 = driver.page_source
        soup2 = BeautifulSoup(html2, 'html.parser')
        return soup2

    def get_full_equip_html(artist_names, artist_urls, equip_type='effects-pedals'):
        full_artist_html = {}
        for name, url in zip(artist_names, artist_urls):
            html_data = get_equipment_html(equip_type, url)
            full_artist_html[name] = html_data
        return full_artist_html

    def get_artist_equip_dict(artist_dict):
        full_artist_equip = {}
        for key, value in artist_dict.iteritems():
            artist_info = {}
            equip_names = html_to_lists(value, 'img', 'alt', base_tag='li', base_att='class', base_att_value='eb-grid-item')
            similar_artists = html_to_lists_alt(value, base_tag='a', base_att='data-similar-type', base_att_value='group')
            genres = html_to_lists_alt2(value)
            member_of = html_to_lists_alt(value)
            artist_info['similar artists'] = similar_artists
            artist_info['genres'] = genres
            artist_info['member of'] = member_of
            artist_info['pedals'] = equip_names
            full_artist_equip[key] = artist_info
        return full_artist_equip

    def get_unique_equip_list(input_list):
        unique_equip_list = []
        for x in input_list:
            if not x in unique_equip_list:
                unique_equip_list.append(x)
        return unique_equip_list

    def get_equip_attributes(artist_dict):
        full_equip_names = []
        full_equip_urls = []
        full_equip_images = []
        for key, value in artist_dict.iteritems():
            equip_names = html_to_lists(value, 'img', 'alt', base_tag='li', base_att='class', base_att_value='eb-grid-item')
            equip_urls = html_to_lists(value, 'a', 'href', base_tag='li', base_att='class', base_att_value='eb-grid-item')
            equip_images = html_to_lists(value, 'img', 'src', base_tag='li', base_att='class', base_att_value='eb-grid-item')
            for name,url,img in zip(equip_names,equip_urls,equip_images):
                if not name in full_equip_names:
                    full_equip_names.append(name)
                    full_equip_urls.append(url)
                    full_equip_images.append(img)
        full_equip_names = get_unique_equip_list(full_equip_names)
        full_equip_urls = get_unique_equip_list(full_equip_urls)
        full_equip_images = get_unique_equip_list(full_equip_images)
        return (full_equip_names, full_equip_urls, full_equip_images)

artist_equipment_dict = get_artist_equip_dict(artist_html_dict)
equipment_names, equipment_urls, equipment_images = get_equip_attributes(artist_html_dict)
