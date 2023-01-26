#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import streamlit as st
import time
warnings.filterwarnings('ignore')

data= pd.read_excel("base article.xlsx")
data= data.fillna(0)
l=[]
ll=[]
liste =[]

