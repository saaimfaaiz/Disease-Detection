# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 02:12:28 2024

@author: KIIT
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('C:/deploying machine learning model/diabetes_trained_model.sav'))

heart_disease_model = pickle.load(open('C:/deploying machine learning model/heart_disease_model.sav'))

parkinsons_model = pickle.load(open('C:/deploying machine learning model/parkinsons_model.sav'))

#sidebar for navigation

with st.sidebar:
    
    selected = options_menu('Multiple Disease Prediction System',
                            ['Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Parkinsons Prediction'].
                            default_index=0)