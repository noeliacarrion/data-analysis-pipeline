import pandas as pd

def open_data(file):
    df = pd.read_csv(file)
    return df
data = open_data('../Input/MissingMigrants.csv')