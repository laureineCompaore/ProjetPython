#Importation des bibliothèques

from dotenv import load_dotenv
import os
import sys
import requests
import json
import logging
import time
import pandas as pd
from pandas import json_normalize
import geopandas as gpd
from io import StringIO
import seaborn as sns
import folium
import json
import requests
import time

#load_dotenv()  # Charge les variables d'environnement du fichier .env

#APPLICATION_ID= os.getenv("APPLICATION_ID")

logging.captureWarnings(True)
# Example of a Python implementation for a continuous authentication client.
# It's necessary to :
# - update APPLICATION_ID
# - update request_url at the end of the script

# unique application id : you can find this in the curl's command to generate jwt token 
APPLICATION_ID = 'Q2Y4QzFxODZ6Ukd4VWhjNzY0aWpOc1NmM1dFYTp3OGdxNXhhMDY5dDl0OXJudFdPYjRveGpzbzBh'

# url to obtain acces token
TOKEN_URL = "https://portail-api.meteofrance.fr/token"

class Client(object):

    def __init__(self):
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        # First request will always need to obtain a token first
        if 'Authorization' not in self.session.headers:
            self.obtain_token()

        # Optimistically attempt to dispatch reqest
        response = self.session.request(method, url, **kwargs)
        if self.token_has_expired(response):
            # We got an 'Access token expired' response => refresh token
            self.obtain_token()
            # Re-dispatch the request that previously failed
            response = self.session.request(method, url, **kwargs)

        return response

    def token_has_expired(self, response):
        status = response.status_code
        content_type = response.headers['Content-Type']
        repJson = response.text
        if status == 401 and 'application/json' in content_type:
            repJson = response.text
            if 'Invalid JWT token' in repJson['description']:
                return True
        return False

    def obtain_token(self):
        # Obtain new token
        data = {'grant_type': 'client_credentials'}
        headers = {'Authorization': 'Basic ' + APPLICATION_ID}
        access_token_response = requests.post(TOKEN_URL, data=data, verify=False, allow_redirects=False, headers=headers)
        token = access_token_response.json()['access_token']
        # Update session with fresh token
        self.session.headers.update({'Authorization': 'Bearer %s' % token})

client = Client()
 # Issue a series of API requests an example. For use this test, you must first subscribe to the arome api with your application
client.session.headers.update({'Accept': 'application/json'})







#fonctions pour générer un numéro de commande


def gener_idcommande(datedebut,datefin):

   client=Client()
   response1 = client.request('GET', 'https://public-api.meteofrance.fr/public/DPClim/v1/commande-station/quotidienne?id-station=01014002&date-deb-periode={}T14%3A30%3A00Z&date-fin-periode={}T14%3A30%3A00Z'.format(datedebut,datefin), verify=False)
   response1=response1.json()
   #print(response1)
   return int((response1.get('elaboreProduitAvecDemandeResponse')).get('return'))


#focntion pour générer une base de données en choisissant les dates 

def gener_data(datedebut,datefin):
     client=Client()
     return client.request('GET',"https://public-api.meteofrance.fr/public/DPClim/v1/commande/fichier?id-cmde={}".format(gener_idcommande(datedebut,datefin)),verify=False)


#fonction pour représenter la carte
def interactive_map_dpe(dpe):

    center = dpe[["lat", "lon"]].mean().values.tolist()
    sw = dpe[["lat", "lon"]].min().values.tolist()
    ne = dpe[["lat", "lon"]].max().values.tolist()

    m = folium.Map(location=center, tiles="OpenStreetMap")

    # I can add markers one by one on the map
    for i in range(0, len(dpe)):
        folium.Marker(
            [dpe.iloc[i]["lat"], dpe.iloc[i]["lon"]],
            icon=folium.Icon(
                color="black", icon="cloud"
            ),
        ).add_to(m)

    m.fit_bounds([sw, ne])

    return m
