import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def open_data(file):
    df = pd.read_csv(file)
    return df

def mean(data, colum):
    mean = data[colum].mean()
    return mean

def plot1(data, lista,columsort, columx, columy):
    data_mean = data.groupby(lista).mean().sort_values(by=columsort)
    data_mean.plot(kind='scatter',x=columx,y=columy,color='red')
    plt.savefig('data_mean_max.png')
    return data_mean

def plot2(data, lista,columsort, columx, columy):
    data_mean = data.groupby(lista).mean().sort_values(by=columsort)
    data_mean.plot(kind='scatter',x=columx,y=columy,color='red')
    plt.savefig('data_mean_min.png')
    return data_mean

def select_columns(data_analysis,column_names):
    new_frame = data_analysis.loc[:, column_names]
    return new_frame

def crosstable(dataFiltered, colum1, colum2, listaCrossTable):
    table_cross = pd.crosstab(dataFiltered[colum1], dataFiltered[colum2], margins=True, margins_name="Total")
    dataplot_final = table_cross[listaCrossTable]
    dataplot_final.plot(kind="bar", figsize=(7,7), stacked=True)
    plt.savefig('data_country_dead.png')
    return dataplot_final

