import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from api import *

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
print(data)
