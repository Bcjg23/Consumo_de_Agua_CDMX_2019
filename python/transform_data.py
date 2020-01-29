#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np


def split_string_column_into_numeric_columns(df, column_name, separator, new_cols_name):
    """
    This function splits the value in a column data frame that has string values into a separate numeric columns 
    
    params: df_name is a dataframe that contains the column we want to split
            colum_name is a string with the name of the column we want to split
            separtor is a string that contains the separator
            new_cols_name is a string list that contains the names for the splitted cols
    
    returns: df with the original column and the new columns named as in new_cols_name
    """
    #Split the column
    df[new_cols_name] =  df.loc[:, column_name ].str.split(separator, expand = True)
    
    for name in new_cols_name:
        df[name] = pd.to_numeric(df[name])
    
    return df



def clean_variables_values(df, columns_names):
    """
    Clean the values of the selected columns: lowercase, no spaces, no accent marks
    
    param: df is a dataframe where the variables to clean are
           colum_names is a list with the name of the variables we are going to clean
    return: df with clean colums
    """
    for name in columns_names:
        df[name] = df[name].str.strip().str.lower().str.replace('.','').str.replace(',','').str.replace(';','').str.replace(' ','_').str.replace('á','a').str.replace('é','e')      .str.replace('í','i').str.replace('ó','o').str.replace('ú','u').str.replace('ñ','n') 
    
    return df
