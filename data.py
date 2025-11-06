import pandas as pd
import numpy as np
import os

def load_gdp_data(path):
    """Load GDP Excel data"""
    df = pd.read_excel(path)
    return df

def clean_gdp_data(df):
    """Clean and preprocess GDP data"""
    df_clean = df.copy()
    
    # Handle missing values with mean imputation
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_clean[col].isnull().sum() > 0:
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)
    
    # Log transformation for GDP columns
    gdp_cols = [col for col in numeric_cols if col != 'Year']
    for col in gdp_cols:
        if (df_clean[col] > 0).all():
            df_clean[f'log_{col}'] = np.log(df_clean[col])
    
    return df_clean

def get_data_summary(df):
    """Get basic data summary"""
    summary = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_stats': df.describe()
    }
    return summary