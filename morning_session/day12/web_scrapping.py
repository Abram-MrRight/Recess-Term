"""
pip install beautifulsoup4
pip install beautifulsoup


"""
# https://xeno-canto.org/
# https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
#https://pypi.org/project/beautifulsoup4/
from bs4 import BeautifulSoup
import requests

url = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'
response = requests.get(url)

# Get Title of the website

soup = BeautifulSoup(response.content , 'html.parser')

title = soup.find('title')
print(title)

# Today's Assignment A12
# Extract all birds species from this website url https://xeno-canto.org/ and generate
# the csv file  or JSON file format for the bird species, family and more
# Extract all birds songs from this website url https://xeno-canto.org/
# use this API to get data. The endpoint for the webservice is at https://xeno-canto.org/api/2/recordings


"""
# Todays assignment

# extract all bird species from the website and generate the csv file and json formart for the bird species, family and more.

# extract all songs from the website

# use this API to get data. the end point is http://xeno-canto.org/api/2/recordings

# Github email: jeff.geoff.mis@gmail.com


"""


import requests
import pandas as pd

def get_bird_species():
    endpoint = 'https://xeno-canto.org/api/2/recordings'
    response = requests.get(endpoint)
    data = response.json()
    return data['recordings']

def get_bird_songs(species):
    endpoint = f'https://xeno-canto.org/api/2/recordings?query={species}'
    response = requests.get(endpoint)
    data = response.json()
    return data['recordings']

def main():
    bird_species = get_bird_species()
    bird_data = []

    for species in bird_species:
        bird_name = species['en']
        bird_songs = get_bird_songs(bird_name)
        bird_data.append({
            'species': bird_name,
            'songs': bird_songs
        })

    df = pd.DataFrame(bird_data)
    df.to_csv('bird_species.csv', index=False)
    # Alternatively, save as JSON
    # df.to_json('bird_species.json', orient='records')

if __name__ == "__main__":
    main()

