import pandas as pd
import re
from acquisition import *

def dropcolumns(data, columns):
        data = data.drop(columns, axis=1)
        return data

def cleanCauseDeath(cause):
    cause = str(cause)
    if (re.search('\s*([Dd]rowning)\s*', cause)):
        return 'Drowning'
    elif (re.search('Unknown', cause)):
        return 'Unknown'
    elif (re.search('\s*([Ss]ickness)|(cancer)|(illness)|(Pneumonia)|(edema)|(partum)|(artery)|(Hypoglycemia)|([Oo]rgan)|([Mm]alnutrition)\s*', cause)):
        return 'Sickness and lack of access to medicines'
    elif (re.search('\s*([Sh]hot)|([Aa]buse)|([Rr]ape)|([Kk]illed)|([Pp]oison)|([Mm]urdered)|(Gassed)|(Violence)|(Envenomation)|([Ss]tabbed)|([Aa]ttack)|([Bb]urned)|([Hh]ang)\s*', cause)):
        return 'Murdered'
    elif (re.search('\s*([Ff]ire)\s*|(Electrocution)|([Cc]rush)|([Hh]it)|([Ff]all)|([Aa]ccident)|([Rr]ock)|(Plane)', cause)):
        return 'Accident'
    elif (re.search('\s*([Ss]tarvation)\s*', cause)):
        return 'Starvation'
    elif (re.search('\s*([Dd]ehydration)\s*', cause)):
        return 'Dehydration'
    elif (re.search('\s*([Hh]ypothermia)|([Hh]yperthermia)|(weather)|(Heat)|(bolt)\s*', cause)):
        return 'Weather conditions'
    elif (re.search('\s*([Aa]sphyxiation)', cause)):
        return 'Asphyxiation'
    elif (re.search('\s*([Sd]uffocation)', cause)):
        return 'Suffocation'
    elif (re.search('([Hh]arsh)|(Exhaustion)|(Exposure)|([Bb]urn)', cause)):
          return 'Harsh conditions'
    else:
        return cause

def cleanLocation(location):
    location = str(location)
    if (re.search('\s*([Pp]ima)|([Aa]rizona\s*)', location)):
        return 'Arizona, USA'
    elif (re.search('\s*([Ss]ahara)\s+([Dd]esert)\W+(Libya)\s*', location)):
          return 'Sahara desert, Libya'
    elif (re.search('\s*([Ss]ahara)\s+([Dd]esert)\W+(Sudan)\s*', location)):
        return 'Sahara desert, Sudan'
    elif (re.search('(Sahara desert|Sudan)', location)):
        return 'Sahara desert, Sudan'
    elif (re.search('(Iran)', location)):
        return 'Iran'
    elif (re.search('Lesvos', location)):
        return 'Lesvos, Greece'
    elif (re.search('Mexico', location)):
        return 'Mexico'
    elif (re.search('Syria', location)):
        return 'Syria'
    elif (re.search('Egypt', location)):
        return 'Egypt'
    elif (re.search('(Libya)|(Tripoli)', location)):
        return 'Libya'
    elif (re.search('Niger', location)):
        return 'Niger'
    elif (re.search('Mali', location)):
        return 'Mali'
    elif (re.search('(Texas)|(Rio Grande)', location)):
        return 'Texas, USA'
    elif (re.search('Greece', location)):
        return 'Greece'
    elif (re.search('California', location)):
        return 'California, USA'
    elif (re.search('Burkina Faso', location)):
        return 'Burkina Faso'
    elif (re.search('Afghanistan', location)):
        return 'Afghanistan'
    elif (re.search('Somalia', location)):
        return 'Somalia'
    elif (re.search('Ethiopia', location)):
        return 'Ethiopia'
    elif (re.search('Algeria', location)):
        return 'Algeria'
    elif (re.search('Ghana', location)):
        return 'Ghana'
    elif (re.search('Turkey', location)):
        return 'Turkey'
    elif (re.search('(Spain)|(Canary Islands)|(Ceuta)|(Melilla)', location)):
        return 'Spain'
    elif (re.search('(Italy)|(Sicily)', location)):
        return 'Italy'
    elif (re.search('France', location)):
        return 'France'
    elif (re.search('Yemen', location)):
        return 'Yemen'
    elif (re.search('Colombia', location)):
        return 'Colombia'
    elif (re.search('Morocco', location)):
        return 'Morocco'
    elif (re.search('Bangladesh', location)):
        return 'Bangladesh'
    elif (re.search('(Mexico)|(Tamaulipas)', location)):
        return 'Mexico'
    elif (re.search('Nicaragua', location)):
        return 'Nicaragua'
    elif (re.search('Guatemala', location)):
        return 'Guatemala'
    elif (re.search('Myanmar', location)):
        return 'Myanmar'
    elif (re.search('Serbia', location)):
        return 'Serbia'
    elif (re.search('Honduras', location)):
        return 'Honduras'
    elif (re.search('Puerto Rico', location)):
        return 'Puerto Rico'
    else:
        return location

def FilterNumberCountry(data, col):
    count = data[col].value_counts()
    lista = count[count>5].index.tolist() 
    data = data[data[col].isin(lista)]
    return data

def fillNaN(data, col):
    [data[col].fillna('Unknown', inplace=True) for col in data.columns]
    return data
    