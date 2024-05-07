#!/usr/bin/env python
# coding: utf-8

# In[1]:
import streamlit as st
import pickle


from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


# In[2]:


# Read dataset to pandas dataframe
dataset = pd.read_csv('Employee.csv') 

# Create an instance of LabelEncoder
le = LabelEncoder()

# Fit and transform the 'Education' column
dataset['Education'] = le.fit_transform(dataset['Education'])
dataset['City'] = le.fit_transform(dataset['City'])
dataset['Gender'] = le.fit_transform(dataset['Gender'])
dataset['EverBenched'] = le.fit_transform(dataset['EverBenched'])





X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

x_train,x_test,y_train,y_test=train_test_split(X,y)

gb_model = GradientBoostingClassifier()
gb_model = gb_model.fit(x_train, y_train)

pickle.dump(gb_model,open('gb_model.pkl','wb'))




