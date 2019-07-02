import pandas as pd
import requests
import matplotlib.pyplot as plt

import acquisition

def read_file(file):
    data = acquisition.open_data(file)
    return data

def main():
    data_x = read_file('../Input/MissingMigrants.csv')
    #data_clean = cleaning(data)
    #data_imported = impor(data_clean,"https://restcountries.eu/rest/v2/name/")


#def cleaning(data):

    #dataCopy = data.copy()
    #clean.delete_columns(data_ok,['HDI for year','country-year']) 
    #data_ok = clean.delete_rows_excluding(data_ok,'country','Saint Vincent and Grenadines')
    #data_ok = clean.resetindex(data_ok)
    #return data_ok

#def impor(data,url):
    #languages = importing.apiimportlanguage(data,url)
    #regions = importing.apiimportregion(data,url)
    #listlangu=importing.generatelist(data,'country',languages)
    #listreg=importing.generatelist(data,'country',regions)
    #importing.add_columns(data,'Language',listlangu)
    #importing.add_columns(data,'Region',listreg)
    #return data

#def analyze(data):

if __name__ == "__main__":
    main()