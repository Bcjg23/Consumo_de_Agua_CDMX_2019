#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np


def clean_variables_names(data_frame):
    """
    Clean the name of the columns for the data_frame: lowercase, no spaces, no accent marks
    
    param: data_frame to clean column names
    return: data_frame with clean colum names
    """
    
    data_frame.columns = data_frame.columns.str.strip().str.lower().str.replace(' ','_')                  .str.replace('á','a').str.replace('é','e').str.replace('í','i')                      .str.replace('ó','o').str.replace('ú','u').str.replace('ñ','n')
    return data_frame


