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








def plot_bars(features, target, df):
    '''
    plot_bars(features, target, df):
    - iterates through dataframe columns and plots barcharts for all categorical columns
    args:
        features: list of string column names
        target: string name of target variable column
        df: data frame containing feature and target columns
    '''

    # iterate through feature columns and select columns of object or integer type
    for column in df[features].select_dtypes([object, int, bool]).columns.tolist():
        # check how many unique values column has, if over 5, we won't use column
        if len(df[column].unique()) <= 5:
            # build chart
            sns.barplot(column, target, data=df)
            plt.title(column)
            plt.ylabel(target)
            plt.show()

def plot_violin(features, target, df):
    '''
    
    '''
    for descrete in df[features].select_dtypes([object,int, bool]).columns.tolist():
        if df[descrete].nunique() <= 5:
            for continous in df[features].select_dtypes(float).columns.tolist():
                sns.violinplot(descrete, continous, hue=target,
                data=df, split=True, palette=['blue','orange'])
                plt.title(continous + ' x ' + descrete)
                plt.ylabel(continous)
                plt.show()



















# single violin plot
fig = plt.figure(figsize=(5,4))
gs = gridspec.GridSpec(1, 1)
sns.set(font_scale=1.4)
ax1 = plt.subplot(gs[0, 0])
sns.violinplot('Monthly_or_not', 'monthly_charges', hue='churn', data=train, split=True, palette="Dark2", ax = ax1)
plt.title('Relationship among Churn Rate, Contract Type & Monthly Charge')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# name_of_plot.fig.savefig(figure_output_path) 



# multiple plot
features = ['gender', 'partner', 'dependents', 'multiple_lines']
_, ax = plt.subplots(nrows=1, ncols=4, figsize=(20,8))
for i, feature in enumerate(features):
    sns.violinplot(feature, 'monthly_charges', hue='churn', data=train, split=True, ax=ax[i], palette="Dark2")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.suptitle('Churn rates based on features')


features = ['device_protection', 'tech_support', 'paperless_billing', 'internet_service_type']
_, ax = plt.subplots(nrows=1, ncols=4, figsize=(20,8))
for i, feature in enumerate(features):
    sns.violinplot(feature, 'monthly_charges', hue='churn', data=train, split=True, ax=ax[i], palette="Dark2")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    
features = ['contract_type', 'payment_type']
_, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,8))
for i, feature in enumerate(features):
    sns.violinplot(feature, 'monthly_charges', hue='churn', data=train, split=True, ax=ax[i], palette="Dark2")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.xticks(rotation=-80)
plt.show()


# cat & cat
for i in train.drop(columns='churn'):
    sns.barplot(x=i, y='churn', data=train, color='Blue')
    plt.show()

sns.barplot(x="prod_phone_service", y="monthly_charges",data=train_red,hue="churn")
plt.legend()
plt.hlines(y=train_red.monthly_charges.mean(), xmin=-1, xmax=3, ls=":")


# categorical & continuous
sns.swarmplot(x="online_security_backup", y="monthly_charges", data=train_df, hue="churn", palette="Set2")
ax = sns.boxplot(x="online_security_backup", y="monthly_charges", data=train_df,
        showcaps=True,boxprops={'facecolor':'None'},
        showfliers=True,whiskerprops={'linewidth':0})