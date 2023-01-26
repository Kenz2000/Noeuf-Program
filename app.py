#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
from hom import home
import data_init
from User_input import user_input
from User_input import user_add
from User_input import user_supp
from estimation import estimation
from estimation import calcul_total
import plotly.express as px

def main() :
        d=home()
        st.title('menu')
        status = st.radio("Choisir : ", ('Consulter base article', 'Consulter les quantités projets','estimation',
                                         'Inserer des quantités projets','ajouter un article de base','supprimer un article de base'))
        if (status == 'Consulter base article'):
            test = (d).astype(str)
            st.dataframe(test)
        elif (status == 'Inserer des quantités projets'):      
                        user_input(data_init.data)
                           
        elif (status == 'Consulter les quantités projets'):   
                        data= pd.read_excel("Quantités Projet.xlsx")
                        data= data.fillna(0)
                        test = (data).astype(str)
                        st.dataframe(test)
        elif (status == 'estimation'):   
                        dat= pd.read_excel("Quantités Projet.xlsx")
                        dat= dat.fillna(0)
                        calcul_total(dat,data_init.data)
                        
                        

        elif (status == 'ajouter un article de base'):
                        df=user_add(data_init.data)
                        df.fillna(0)
                        df.to_excel("bases articles.xlsx")
                        test = (df).astype(str)
                        st.dataframe(test)
        elif (status == 'supprimer un article de base'):
                        df=user_supp(data_init.data)
                        df.fillna(0)
                        df.to_excel("bases articles.xlsx")
                        test = (df).astype(str)
                        st.dataframe(test)
                        
        else :
            st.write("yes")
            
if __name__ == '__main__' :
    main()

