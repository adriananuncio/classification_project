import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import acquire


df = acquire.get_telco_data()

def clean_data(df):
    '''This function will take in a dataframe and search for 
'payment_type_id', 'internet_service_type_id',  'contract_type_id'.
If the specified columns are in the dataset,  drop_cols in the if 
statement will be executed.
If the specified columns are not in the dataset, drop_cols in the 
else statement will execute.
For columns in dummy_col, dummy columns will be created
without dropping the first column.
For columns in dummies, dummy columns will be created and the 
first columns will be dropped
Dummy columns from dummy_col will first be concated to the 
original dataframe, then dummy columns from dummies will be 
concated to the dataframe created by dummy_col and the original 
dataframe.
Column names are then formatted to be lowercase, and spaces in 
column names are changed to underscores.
Lastly, the appropriate drop_cols is executed, and specified 
columns are renamed'''
    dummies = ['gender'
               , 'partner'
               , 'dependents']
    if 'payment_type_id' or 'internet_service_type_id' or 'contract_type_id' in df.columns:
        drop_cols = ['payment_type_id'
                     , 'internet_service_type_id'
                     , 'contract_type_id'
                     , 'multiple_lines'
                     , 'contract_type'
                     , 'internet_service_type'
                     , 'payment_type'
                     , 'online_security'
                     , 'online_backup'
                     , 'device_protection'
                     , 'tech_support'
                     , 'streaming_tv'
                     , 'streaming_movies'
                     , 'gender'
                     , 'partner'
                     , 'dependents'
                     , 'phone_service'
                     , 'paperless_billing'] 
        dummy_1 = pd.concat([df,
            pd.get_dummies(df[dummies], drop_first=True)], axis=1)
        dummy_1.columns = dummy_1.columns.str.lower().str.replace(' ', '_')
    else:
        drop_cols = ['multiple_lines'
                     , 'contract_type' 
                     , 'internet_service_type' 
                     , 'payment_type'
                     , 'online_security'
                     , 'online_backup'
                     , 'device_protection'
                     , 'tech_support'
                     , 'streaming_tv'
                     , 'streaming_movies'
                     , 'gender'
                     , 'partner'
                     , 'dependents'
                     , 'phone_service'
                     , 'paperless_billing']
        dummy_1 = pd.concat([df,
            pd.get_dummies(df[dummies], drop_first=True)], axis=1)
        dummy_1.columns = dummy_1.columns.str.lower().str.replace(' ', '_')
    return dummy_1.drop(columns= drop_cols).rename(columns= {'gender_male': 'is_male'
                                                             , 'partner_yes': 'has_partner'
                                                             , 'dependents_yes': 'has_dependents'})



def split_data(df):
    train, test = train_test_split(df
                               , test_size=.2
                               , random_state=123
                               , stratify=df.churn)
    train, validate = train_test_split(train
                                , test_size=.3
                                , random_state=123
                                , stratify=train.churn)
    return train, validate, test


def prep_telco(df):
    df = clean_data(df)
    train, validate, test = split_data(df)
    return train, validate, test
