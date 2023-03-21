#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Establish connection to Codeup database
from env import host, user, password
import os
import acquire

# data prep
import prep

# data manipulation
import pandas as pd
import numpy as np

# modeling
import seaborn as sns
import matplotlib.pyplot as plt

def figs(train):
    plt.figure(figsize=(15,15))
    # churn x has_partner
    plt.subplot(421)
    plt.title('churn x has_partner')
    sns.barplot(x="has_partner", y="churn", data=train)
    plt.legend
    print('has_partner:' f'\n{train.has_partner.describe()}\n')
    # churn x has_dependents
    plt.subplot(422)
    plt.title('churn x has_dependents')
    sns.barplot(x="has_dependents", y="churn", data=train)
    plt.legend
    print('has_dependents:' f'\n{train.has_dependents.describe()}\n')
    # churn x is_male
    plt.subplot(423)
    plt.title('churn x is_male')
    sns.barplot(x="is_male", y="churn", data=train)
    plt.legend
    print('is_male:' f'\n{train.is_male.describe()}\n')
    plt.tight_layout()


# In[ ]:




