# 2022 0920

# How To Find Seasonality Using Python
# https://datastud.dev/posts/python-seasonality-how-to
import pandas as pd
import numpy as np
import statsmodels.api as sm

import datetime

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# Load Data
df = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Weather Demand\Python example\Kansas_City_Crime__NIBRS__Summary.xlsx', sheet_name = 'Sheet1')

# Choose only necessary columns
df = df[['Date', 'Burglary/Breaking and Entering']]

# Normalize Metric
# df['Burglary/Breaking and Entering'] = df['Burglary/Breaking and Entering'] / pd.to_datetime(df['Date']).dt.day

# Set date index

def set_date_index(input_df, col_name='Date'):
    """Given a pandas df, parse and set date column to index.
        col_name will be removed and set as datetime index.

    Args:
        input_df (pandas dataframe): Original pandas dataframe
        col_name (string): Name of date column

    Returns:
        pandas dataframe: modified and sorted dataframe
    """
    # Copy df to prevent changing original
    modified_df = input_df.copy()

    # Infer datetime from col
    modified_df[col_name] = pd.to_datetime(modified_df[col_name])

    # Sort and set index
    modified_df.sort_values(col_name, inplace=True)
    modified_df.set_index(col_name, inplace=True)

    return modified_df

df = set_date_index(df, 'Date') # custom helper function

# Seasonal decompose
sd = seasonal_decompose(df, period=12)

def combine_seasonal_cols(input_df, seasonal_model_results):
    """Adds inplace new seasonal cols to df given seasonal results

    Args:
        input_df (pandas dataframe)
        seasonal_model_results (statsmodels DecomposeResult object)
    """
    # Add results to original df
    input_df['observed'] = seasonal_model_results.observed
    input_df['residual'] = seasonal_model_results.resid
    input_df['seasonal'] = seasonal_model_results.seasonal
    input_df['trend'] = seasonal_model_results.trend

combine_seasonal_cols(df, sd) # custom helper function

df.plot()



df.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Weather Demand\Python example\outcome.csv', index =None)
