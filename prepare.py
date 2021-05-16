from pydataset import data
import seaborn as sns
import pandas as pd
import numpy as np
import os
from env import host, user, password, get_db_url



def prep_iris(df):
    '''
    takes in a df of the iris dataset as it is acquired and returns a cleaned df
    arguements: df: a pandas df with the expected feature names and columns return: 
    clean_df: a dataframe with the cleaning operations performed on it
    '''
    df = df.drop_duplicates()
    df = df.drop(columns = ['species_id'])
    df = df.rename(columns={"species_name": "species"})
    dummy_species_name = pd.get_dummies(df[['species']]) 
    return df