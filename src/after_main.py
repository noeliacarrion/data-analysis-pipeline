import pandas as pd
import requests
import matplotlib.pyplot as plt
import acquisition 
import clean
#import api

def read_file(file):
    my_dataframe = acquisition.open_data(file)
    return my_dataframe

def cleaning(my_dataframe):
    columns_deleted =['Web ID','Reported Date', 'Information Source', 'URL', 'UNSD Geographical Grouping', 'Source Quality']
    my_dataframe = clean.dropcolumns(my_dataframe,columns_deleted)
    my_dataframe['Cause of Death'] = my_dataframe['Cause of Death'].apply(clean.cleanCauseDeath)
    my_dataframe['Location Description'] = my_dataframe['Location Description'].apply(clean.cleanLocation)
    my_dataframe = clean.FilterNumberCountry(my_dataframe, 'Location Description')
    my_dataframe = clean.fillNaN(my_dataframe,'Number of Females')
    return my_dataframe

#  def datafromApi(my_dataframe):
#     my_dataframe['latitud'] = my_dataframe['Location Coordinates'].apply(api.get_lat) 
#     my_dataframe['latitud'] = my_dataframe['Location Coordinates'].apply(api.get_lat)
#     my_dataframe['longitud'] = my_dataframe['Location Coordinates'].apply(api.get_lon)
#     lista_marzo = api.Apidata([])
#     lista_febrero = api.Apidata1([])
#     lista_enero= api.Apidata2([])
#     lista_diciembre = api.Apidata3([])
#     lista_noviembre = api.Apidata4([])

#     return my_dataframe

data = read_file('../Input/MissingMigrants.csv')
data_clean = cleaning(data)

if __name__ == "__main__":
    main()
    
