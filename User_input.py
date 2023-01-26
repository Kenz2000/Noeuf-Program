#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import pandas as pd
import time
import data_init

def user_input(data):
                        dataPres= data[(data['Désignation'].str.contains("Pose|Dépose|Mise|Installation|Déplacement|mise|Remplacement|Parametrage|déroulement|supervision|programmation"))]
                        dataEq=data[(data['Désignation'].str.contains("Pose|Dépose|Mise|Installation|Déplacement"))==False]
                        st.sidebar.header("Remplissage des quantité de projet")
                        my_date=st.sidebar.date_input('date')
                        titre=st.sidebar.text_input('Nom du projet')
                        sys=st.sidebar.selectbox('choisir un sous systeme',data['Ssysteme'].unique())
                        liste=((dataPres[dataPres['Ssysteme']==sys])["Désignation"]).unique()
                        prestation= st.sidebar.selectbox('choisir une prestation',liste)
                        liste1=((dataEq[dataEq['Ssysteme']==sys])["Désignation"]).unique()
                        equipement= st.sidebar.selectbox('choisir un equipement ',liste1)
                        ChapCCTP=st.sidebar.text_input("Chapitre CCTP:")
                        NumEq=st.sidebar.text_input("Numero de l'equipement")
                        local=st.sidebar.text_input("Localisation")
                        qteJour=st.sidebar.number_input('choisir la quantité Jour ', 0,500)
                        qteNuit=st.sidebar.number_input('choisir la quantité Nuit', 0,500)
                        comment=st.sidebar.text_area('Commentaire')
                        d={"Chap CCTP":ChapCCTP,"Prestations":prestation,"Equipement":equipement,"N°Eqp":NumEq,"Qté Nuit":qteNuit,
                           "Qté Jour":qteJour,"localisation":local,"Ssysteme":sys,"Commentaire":comment}
                        if st.sidebar.button('Ajouter'):
                                data_init.l.append(d)
                                df=pd.DataFrame(data_init.l)
                                df.dropna(inplace=True)
                                test = (df).astype(str)
                                test.to_excel("Quantités Projet.xlsx")
                                st.dataframe(test)
                                
                        else:
                                pass
def user_add(data):
        sys=st.sidebar.selectbox('choisir un sous systeme',data['Ssysteme'].unique())
        designation= st.sidebar.text_input("Désignation")
        numRef=st.sidebar.text_input("N°Réf")
        unité=st.sidebar.text_input("Unité")
        Fourniture=st.sidebar.text_input("Fourniture")
        qteForfait=st.sidebar.text_input("Qté Forfait")
        qteJour=st.sidebar.text_input("MO (J)")
        qteNuit=st.sidebar.text_input("MO (N)")
        ChapCCTP=st.sidebar.text_input("Chapitre CCTP:")
        d={"Chap CCTP":ChapCCTP,"Désignation":designation,"N°Réf":numRef,"Unité":unité,"Fourniture":Fourniture,"MO (J)"                                   :qteJour,"MO (N)":qteNuit,"Ssysteme":sys}
        
        if st.sidebar.button('Ajouter'):
            data=data.append(d, ignore_index=True)
            print(data)
            return data
        else:
             return data
def user_supp(data):
        num= st.sidebar.text_input("La référence de l'article a supprimer :")
        if st.sidebar.button('Supprimer'):
            data= data[data["N°Réf"]!=num]
            print(data)
            return data
        else:
             return data
        