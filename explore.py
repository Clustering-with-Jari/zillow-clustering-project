import pandas as pd 
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


def df_feature_box(df):
    # get a list of columns where content is number
    features_num = list(df.select_dtypes(np.number).columns)
    # boxplot to vis outliers
    for feature in features_num:
        sns.boxplot(df[feature].dropna())
        plt.show()