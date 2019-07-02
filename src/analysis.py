import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def twoDataframes(data_apis, data_clean):
    data_apis = data_apis.reset_index(drop=True, inplace=True)
    data_filter = data_clean[0:255]
    data_analysis = pd.concat([data_filter, data_apis], axis=1)
    return data_analysis

def select_columns(data_analysis,column_names):
    new_frame = data_analysis.loc[:, column_names]
    return new_frame