import pandas as pd
import requests
import matplotlib.pyplot as plt
import acquisition 
import clean
import api
import analysis
import os

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
    my_dataframe = my_dataframe.reset_index()

    return my_dataframe

def datafromApi(my_dataframe):
    my_dataframe['latitud'] = my_dataframe['Location Coordinates'].apply(api.get_lat) 
    my_dataframe['longitud'] = my_dataframe['Location Coordinates'].apply(api.get_lon)
    data_marzo = api.Apidata(my_dataframe)
    data_febrero = api.Apidata1(my_dataframe)
    data_enero = api.Apidata2(my_dataframe)
    data_diciembre = api.Apidata3(my_dataframe)
    data_noviembre = api.Apidata4(my_dataframe)
    data_apis = api.makeData([data_marzo, data_febrero, data_enero, data_diciembre, data_noviembre])
    data_merge = api.twoDataframes(data_apis, my_dataframe)
    selected_columns = api.select_columns(data_merge, ['Reported Month','temperatureMin', 'Total Dead and Missing','Region of Incident'])
    data_merge.to_csv(os.path.dirname(os.path.realpath(__file__))+'/DataMerge.csv', encoding='utf-8', index=False)

    return selected_columns

#def analysis(data_apis, data_clean):
    #data_merge = analysis.twoDataframes(data_apis, data_clean)
    #selected_columns = analysis.select_columns(data_merge, ['Reported Month','temperatureMin', 'Total Dead and Missing','Region of Incident'])
    #data_merge.to_csv(os.path.dirname(os.path.realpath(__file__))+'/DataMerge.csv', encoding='utf-8', index=False)

    #return selected_columns

def analysis_plot():
    data_plot = analysis.open_data('../src/DataMerge.csv')
    mean_data = analysis.mean(data_plot, 'temperatureMax')
    data_plot1 = analysis.plot1(data_plot, ['Reported Month', 'Region of Incident'], 'temperatureMax','temperatureMax', 'Total Dead and Missing')
    data_plot2 = analysis.plot2(data_plot, ['Reported Month', 'Region of Incident'], 'temperatureMin','temperatureMin', 'Total Dead and Missing')
    selected_columns = analysis.select_columns(data_plot,['Region of Incident','temperatureMax', 'Cause of Death'])
    crosstable_plot = analysis.crosstable(selected_columns, 'Region of Incident','Cause of Death', ['Accident','Cardiac arrest','Dehydration','Murdered','Sickness and lack of access to medicines','Suffocation','Unknown','Weather conditions'])

    return mean_data, data_plot1, data_plot2, crosstable_plot
