import pandas as pd
import numpy as np
import os

#visualize
import seaborn as sns
import matplotlib.pyplot as plt

#acquire
from env import host, user, password
from pydataset import data




# Make a new python module, acquire.py to hold the following data aquisition functions:


# 1.  Make a function named get_titanic_data that returns the titanic data from the codeup 
# data science database as a pandas data frame. Obtain your data from the Codeup Data 
# Science Database.

def get_connection(db_name):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}

 
#### Titanic data #####    

def  get_new_titanic_data():
    '''
    This function reads in the titanic data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = 'SELECT * FROM passengers'
    return pd.read_sql(sql_query, get_connection('titanic_db'))



def get_titanic_data(cached=False):
    '''
    This function reads in titanic data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in titanic df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('titanic_df.csv') == False:
        
        # Read fresh data from db into a DataFrame.
        df = new_titanic_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('titanic_df.csv')
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    return df


# 2. Make a function named get_iris_data that returns the data from the iris_db on the 
# codeup data science database as a pandas data frame. The returned data frame should 
# include the actual name of the species in addition to the species_ids. Obtain your 
# data from the Codeup Data Science Database.

def get_new_iris_data():
    '''
    This function reads in the iris data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = '''
    SELECT *
    FROM measurements
    JOIN species USING (species_id)
    '''
    return pd.read_sql(sql_query, get_connection('iris_db'))



def get_iris_data(cached=False):
    '''
    This function reads in titanic data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in titanic df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('titanic_df.csv') == False:
        
        # Read fresh data from db into a DataFrame.
        df = get_new_iris_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('iris_df.csv')
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('iris_df.csv', index_col=0)
        
    return df


