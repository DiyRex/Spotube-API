import requests
from bs4 import BeautifulSoup
import time
import re
import string
import json
import query



def spotify_dl(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('title')
    song_name = data.text[:-10]
    data_dt = soup.find('meta',attrs={'property': 'og:description'} )
    data_img = soup.find('meta',attrs={'property': 'og:image'} )['content']



    year = re.search(r"\d{4}", data_dt['content']).group(0)
    # print(year)

    song_title = song_name.split("-")[0].rstrip()
    song_artist = song_name.split("-")[1].lstrip()[7:].lstrip()

    # print(song_title)
    # print(song_artist)

    video_url = query.search(song_title+" "+song_artist)

    res_data = {'Song':song_title,'Author':song_artist,'year':year,'image':data_img,'video_url':video_url}

    return res_data