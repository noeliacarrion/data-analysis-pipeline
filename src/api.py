import pandas as pd
import requests
import os
from clean import *
from dotenv import load_dotenv
load_dotenv()

if not "TOKEN" in os.environ:
    raise ValueError("You should pass a TOKEN")
TOKEN = os.environ["TOKEN"]
BASE_URL= "https://api.darksky.net/forecast"

def get_lat_lon(st): 
    try: 
        st = st.replace('[', '').replace(']', '') # fuera corchetes
        lat, lon = st.split(',')
        res = {'latitud': float(lat.strip()), 'longitud': float(lon.strip())}
    except: 
        res = {'latitud': 0, 'longitud': 0}
    return res

def get_lat(st): 
    return get_lat_lon(st).get('latitud')
def get_lon(st): 
    return get_lat_lon(st).get('longitud')

data['latitud'] = data['Location Coordinates'].apply(get_lat)
data['longitud'] = data['Location Coordinates'].apply(get_lon)

def get_3_items(data, ind_row): 
    latitud = data.loc[ind_row, 'latitud']
    longitud = data.loc[ind_row, 'longitud']
    return (latitud, longitud)

def Apidata(lista):
    lista_marzo=[]
    for ind in range(31): 
        lat, lon = get_3_items(data, ind)
        res = requests.get("{}/{}/{},{},1551398400?exclude=currently,flags, minutely, hourly".format(BASE_URL, TOKEN, lat, lon))
        temperatureMax = res.json().get('daily').get('data')[0].get('temperatureMax')
        temperatureMin = res.json().get('daily').get('data')[0].get('temperatureMin')
        uvIndex = res.json().get('daily').get('data')[0].get('uvIndex')
        diccion ={}
        diccion.update({"temperatureMax": temperatureMax, "temperatureMin": temperatureMin, "uvIndex": uvIndex})
        lista_marzo.append(diccion)
        return lista_marzo

def Apidata1(url):
    lista_febrero=[]
    for ind in range(32,76): 
        lat, lon = get_3_items(data, ind)
        res = requests.get("{}/{}/{},{},1548979200?exclude=currently,flags, minutely, hourly".format(BASE_URL, TOKEN, lat, lon))
        return lista_febrero
    
def Apidata2(url):
    lista_enero=[]
    for ind in range(77,132): 
        lat, lon = get_3_items(data, ind)
        res = requests.get("{}/{}/{},{},1546300800?exclude=currently,flags, minutely, hourly".format(BASE_URL, TOKEN, lat, lon))
        temperatureMax = res.json().get('daily').get('data')[0].get('temperatureMax')
        temperatureMin = res.json().get('daily').get('data')[0].get('temperatureMin')
        uvIndex = res.json().get('daily').get('data')[0].get('uvIndex')
        diccion ={}
        diccion.update({"temperatureMax": temperatureMax, "temperatureMin": temperatureMin, "uvIndex": uvIndex})
        lista_enero.append(diccion) 
        return lista_enero
    
def Apidata3(url):
    lista_diciembre=[]
    for ind in range(133,185): 
        lat, lon = get_3_items(data, ind)
        res = requests.get("{}/{}/{},{},1543622400?exclude=currently,flags, minutely, hourly".format(BASE_URL, TOKEN, lat, lon))
        temperatureMax = res.json().get('daily').get('data')[0].get('temperatureMax')
        temperatureMin = res.json().get('daily').get('data')[0].get('temperatureMin')
        uvIndex = res.json().get('daily').get('data')[0].get('uvIndex')
        diccion ={}
        diccion.update({"temperatureMax": temperatureMax, "temperatureMin": temperatureMin, "uvIndex": uvIndex})
        lista_diciembre.append(diccion)
        return lista_diciembre

def Apidata4(url):
    lista_noviembre=[]
    for ind in range(186,259): 
        lat, lon = get_3_items(data, ind)
        res = requests.get("{}/{}/{},{},1543622400?exclude=currently,flags, minutely, hourly".format(BASE_URL, TOKEN, lat, lon))
        temperatureMax = res.json().get('daily').get('data')[0].get('temperatureMax')
        temperatureMin = res.json().get('daily').get('data')[0].get('temperatureMin')
        uvIndex = res.json().get('daily').get('data')[0].get('uvIndex')
        diccion ={}
        diccion.update({"temperatureMax": temperatureMax, "temperatureMin": temperatureMin, "uvIndex": uvIndex})
        lista_noviembre.append(diccion)
        return lista_noviembre

def makeData(lista):
    data_lista = pd.DataFrame(lista)
    dataframe_merge = pd.concat(data_lista)
    dataframe_merge.reset_index(drop=True, inplace=True)
    return dataframe_merge

def filterdata(data):
    data_filter = data.iloc[0:255]
    data_filter.reset_index(drop=True, inplace=True)
    data_analysis = pd.concat( [data_filter, dataframe_merge], axis=1)
    return data_analysis
