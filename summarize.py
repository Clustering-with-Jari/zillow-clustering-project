import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# This function takes in a dataframe and returns a new two column dataframe. 
# First column returns number of nulls in each row and 
# second column returns percentage of rows missing.

def nulls_by_col(df):
    num_missing = df.isnull().sum()
    rows = df.shape[0]
    pct_missing = num_missing/rows
    cols_missing = pd.DataFrame({'num_rows_missing': num_missing, 'pct_rows_missing': pct_missing}).sort_values("pct_rows_missing", ascending=False)


    plt.figure(figsize=(20,40))
    sns.set(style="whitegrid")
    sns.set_color_codes("muted")
    sns.barplot(x='pct_rows_missing', y= cols_missing.index, data=cols_missing,
            label="Percentage of Missing Value in Each Row", color="b")

    return cols_missing


# This function takes a df and returns another df
# num_rows_of_interest let you pick how many rows do you want to filter
def report_remain_nulls_by_col(df, num_rows_of_interest):
    num_missing = df.isnull().sum()
    rows = df.shape[0]
    pct_missing = num_missing/rows
    cols_missing = pd.DataFrame({'num_rows_missing': num_missing, 'pct_rows_missing': pct_missing})
    cols_missing = cols_missing[cols_missing['num_rows_missing'] > num_rows_of_interest]
    return cols_missing

# This function takes in a dataframe and returns number of missing columns and percentage of missing columns

def nulls_by_row(df):
    num_cols_missing = df.isnull().sum(axis=1)
    pct_cols_missing = df.isnull().sum(axis=1)/df.shape[1]*100
    rows_missing = pd.DataFrame({'num_cols_missing': num_cols_missing, 'pct_cols_missing': pct_cols_missing}).reset_index().groupby(['num_cols_missing','pct_cols_missing']).count().rename(index=str, columns={'index': 'num_rows'}).reset_index()
    return rows_missing

# This function takes in a dataframe and if the dtype of feature is an object, it will return its value counts and if the dtype is numeric, it will bins of the number.

# def df_value_counts(df):
#     counts = pd.Series([])
#     for i, col in enumerate(df.columns.values):
#         if df[col].dtype == 'object':
#             col_count = df[col].value_counts()
#         else:
#             col_count = df[col].value_counts(bins=10, sort=False)
#         counts = counts.append(col_count)
#     return counts
def df_value_counts(df):
    for col in df.columns:
        print(f'{col}:')
        if df[col].dtype == 'object':
            col_count = df[col].value_counts()
        else:
            if df[col].nunique() >= 35:
                col_count = df[col].value_counts(bins=10, sort=False)
            else:
                col_count = df[col].value_counts()
        print(col_count)

# This function will take in a dataframe and return all of the summary information.

def df_summary(df):
    print('--- Shape: {}'.format(df.shape))
    print('--- Info')
    df.info()
    print('--- Descriptions')
    print(df.describe(include='all'))
    print('--- Value Counts')
    print(df_value_counts(df))