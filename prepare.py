import pandas as pd
import scipy.stats as stats
import numpy as np

# Selects single unit properties out of data.
def zillow_single_unit(df):
    criteria_1 = df.propertylandusedesc == 'Single Family Residential'
    #criteria_2=df.unitcnt==1 | df.unitcnt.isna()
    #criteria_2=df.unitcnt==1 & calculatedfinishedsquarefeet>500
    criteria_2 = df.calculatedfinishedsquarefeet > 500
    df = df[(criteria_1) & (criteria_2)]
    return df

# Remove unwanted columns.
def remove_columns(df, cols_to_remove):  
    df = df.drop(columns=cols_to_remove)
    return df

# Remove rows and columns based on a minimum percentage for each row and column.
def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

# Combining both the previous functions together.
def data_prep(df, cols_to_remove=[], prop_required_column=.5, prop_required_row=.75):
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)
    return df

# Fills missing values with 0's where it makes sense.
def fill_zero(df, cols):
    df.fillna(value=0, inplace=True)
    return df

# take out?
def remove_outliers_iqr_old(df, col):

    q1, q3 = df[col].quantile([.25, .75])
    iqr = q3 - q1
    ub = q3 + 3 * iqr
    lb = q1 - 3 * iqr

    df = df[df[col] <= ub]
    df = df[df[col] >= lb]
    return df

# Split the data into train/test 
def split_my_data(data):
    data.fillna(np.nan, inplace=True)
    data = data.dropna()
    from sklearn.model_selection import train_test_split
    return train_test_split(data, train_size = 0.8, random_state = 123)

# 
def impute(train, test, my_strategy, column_list):
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy=my_strategy)
    train[column_list] = imputer.fit_transform(train[column_list])
    test[column_list] = imputer.transform(test[column_list])
    return train, test

# change col_name into take a col_list 
def encode(train, test, col_list):
    from sklearn.preprocessing import LabelEncoder
    
    for col_name in enumerate(col_list):
    # Integer Encoding
        int_encoder = LabelEncoder()
        train[col_name] = int_encoder.fit_transform(train[col_name])
        test[col_name] = int_encoder.transform(test[col_name])
    
    return train, test

# remove outliers 
def remove_outliers_iqr(df, columns):
    for col in columns:
        #q75, q25 = np.percentile(df[col], [75,25])

        q1, q3 = col.quantile([.25, .75])
        iqr = q3 - q1
        ub = q3 + k * iqr
        lb = q1 - k * iqr
        
        df = df[df[col] <= ub]
        df = df[df[col] >= lb]
    return df
