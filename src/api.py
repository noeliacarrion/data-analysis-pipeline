import pandas as pd
import requests
import os
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

def get_3_items(data, ind_row): 
    latitud = data.loc[ind_row, 'latitud']
    longitud = data.loc[ind_row, 'longitud']
    return (latitud, longitud)

def Apidata(data):
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
    data_marzo=pd.DataFrame(lista_marzo)
    return data_marzo

def Apidata1(data):
    lista_febrero=[]
    for ind in range(32,76): 
        lat, lon = get_3_items(data, ind)
        res = requests.get("{}/{}/{},{},1548979200?exclude=currently,flags, minutely, hourly".format(BASE_URL, TOKEN, lat, lon))
        temperatureMax = res.json().get('daily').get('data')[0].get('temperatureMax')
        temperatureMin = res.json().get('daily').get('data')[0].get('temperatureMin')
        uvIndex = res.json().get('daily').get('data')[0].get('uvIndex')
        diccion ={}
        diccion.update({"temperatureMax": temperatureMax, "temperatureMin": temperatureMin, "uvIndex": uvIndex})
        lista_febrero.append(diccion)
    data_febrero=pd.DataFrame(lista_febrero)
    return data_febrero
    
def Apidata2(data):
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
    data_enero = pd.DataFrame(lista_enero)
    return data_enero
    
def Apidata3(data):
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
    data_diciembre = pd.DataFrame(lista_diciembre)
    return data_diciembre

def Apidata4(data):
    lista_noviembre=[]
    for ind in range(186,255): 
        lat, lon = get_3_items(data, ind)
        res = requests.get("{}/{}/{},{},1543622400?exclude=currently,flags, minutely, hourly".format(BASE_URL, TOKEN, lat, lon))
        temperatureMax = res.json().get('daily').get('data')[0].get('temperatureMax')
        temperatureMin = res.json().get('daily').get('data')[0].get('temperatureMin')
        uvIndex = res.json().get('daily').get('data')[0].get('uvIndex')
        diccion ={}
        diccion.update({"temperatureMax": temperatureMax, "temperatureMin": temperatureMin, "uvIndex": uvIndex})
        lista_noviembre.append(diccion)
    data_noviembre = pd.DataFrame(lista_noviembre)
    return data_noviembre

def makeData(lista):
    data_lista = lista
    dataframe_merge = pd.concat(data_lista)
    return dataframe_merge

def twoDataframes(data_apis, data_clean):
    data_apis.reset_index(drop=True, inplace=True)
    data_filter = data_clean.iloc[0:251]
    data_analysis = pd.concat([data_filter, data_apis], axis=1)
    return data_analysis

def select_columns(data_analysis,column_names):
    new_frame = data_analysis.loc[:, column_names]
    return new_frame