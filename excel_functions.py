#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[3]:


def get_files_and_make_dfs():
    '''
    This function gets the users file path, creates a list of data frames and performs operations,
    and then spits out each data frame in the list as a separate data frame. This code below is for specific case 
    (AVC Dashboard, 9/4/2022)
    '''
    # Function to get file path
    file_path = input("FILE PATH:")
    
    # create empty list for file names
    file_names = []

    # loop through file path and append each file path with the file name to a list of file names
    for filename in os.scandir(file_path):
        if filename.is_file():
            file_names.append(filename.path)
            
    # create empty list for dfs
    df_list = []

    # loop through list of file names, which allows you to read in the file itself into a data frame, and append to list
    for filename in file_names:
        df = pd.read_excel(filename, header=[0,1], index_col=0)    # read in excel file, header allows for multilevel cols, and index_col for first column to be index
        df_zeros = df.replace('-', 0)    # Replace dashes with 0s
        df_zs = df_zeros.replace('(Z)', 0)    # Replace (Z)s with 0s
        df_zs.index = df_zs.index.map(lambda x: x.replace('.', ''))    # Replace unwanted characters from index names
        df_zs.index = df_zs.index.map(lambda x: x.lstrip('.\t'))
        df_zs.index = df_zs.index.map(lambda x: x.rstrip('/1'))    # for the flow dfs
        df_zs.index = df_zs.index.map(lambda x: x.rstrip('/3'))    # for the rsn dfs
        df_zs.index = df_zs.index.map(lambda x: x.rstrip('4'))    # for the rsn dfs
        df_list.append(df_zs)   # append each data frame to list
        
    # Loop through list of dataframes and create a dataframe for each element in the list
    for df in range(len(df_list)):
        if '13' in file_path:
            globals()[f"fdf_{df}"] = df_list[df]
        else:
            globals()[f"rdf_{df}"] = df_list[df]


# In[ ]:




