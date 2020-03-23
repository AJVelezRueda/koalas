import pandas as pd


def read_csv(filename, sepator):
    df = pd.read_csv(filename, sep=sepator)
    return df 


def describe(dataframe):
    return dataframe.describe()

def maximum(dataframe):
    return dataframe.max()

def minimum(dataframe):
    return dataframe.min()


koalas.filter(dataframe, lambda it: it.field  > 0)