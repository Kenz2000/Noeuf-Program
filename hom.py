#!/usr/bin/env python
# coding: utf-8
import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import data_init

def home() :
    f=open("Quantité Projet.xlsx",'w')
    f.close()
    st.title ("RATP")
    st.write("WELCOME TO MVP CFA")
    st.image("R.jpg")
    uploaded_file = st.file_uploader("Choisir la base de cout")
    if uploaded_file is not None:
        dataframe = pd.read_excel(uploaded_file)
        dataframe= dataframe.fillna(0)
        return dataframe
    else:
         return data_init.data



