import os
from env import host, user, password
import pandas as pd

    
# This function will establish a callable connection to the Codeup db
def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
# This function will read the telco_churn data, from the Codeup database, to a dataframe.
def telco_data():
    sql_query = '''
        select * from customers
        join contract_types using (contract_type_id)
        join internet_service_types using (internet_service_type_id)
        join customer_payments using (payment_type_id)
        '''
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    return df

# this function will call the telco_churn data from the Codeup db to a csv file
def get_telco_data():
    if os.path.isfile('telco.csv'):
        df = pd.read_csv('telco.csv', index_col=0)
    else:
        df = telco_data()
        df.to_csv('telco.csv')
    return df