import streamlit as st
import pandas as pd
from hom import home
import data_init
from User_input import user_input
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



def estimation(dataQT,data):
    data_init.ll=[]
    data_init.liste=[]
    for i in range(len(dataQT)):
        ligne=data[data["Désignation"]==dataQT.loc[i,'Prestations']]
        ligne1=data[data["Désignation"]==dataQT.loc[i,'Equipement']]
        ligne = ligne.squeeze()
        ligne1 = ligne1.squeeze()
        qte=ligne['Qté Forfait']
        somme1=0
        somme2=0
        des=''
        l=[ligne["N°Réf"],ligne["Ref F1"],ligne["Ref F2"],ligne["Ref F3"],ligne["Ref CB1"],ligne["Ref CB2"],ligne["Ref CB3"],ligne["Ref CB4"]]
        #print(dataQT.loc[i,'Prestations'])
        val=str(dataQT.loc[i,'Prestations'])
        print(val)
        if (val.startswith("Pose")==True):
                print(ligne1['N°Réf'])
                #l.append(ligne1['N°Réf'])
        else:
            pass
        
        d=[]
        my_dict=dict()
        for elem in l:
             if  (elem !=0) :
                    Synth =dict()
                    eq=data[(data["N°Réf"]==elem)].to_dict()
                    Synth["Désignation"]=(list(eq["Désignation"].values()))[0]
                    Synth["Unité"]=(list(eq['Unité'].values()))[0]
                    Synth["Fourniture P.U. (€)"]= (list(eq['Fourniture'].values()))[0]  
                    Synth["M.O Jour P.U. (€)"]=(list(eq["MO (J)"].values()))[0] 
                    Synth["M.O Nuit P.U. (€)"]=(list(eq["MO (N)"].values()))[0]  
                    Synth["Qté Jour"]=dataQT.loc[i,'Qté Jour']
                    Synth["Qté Nuit"]=dataQT.loc[i,'Qté Nuit']
                    if Synth["Unité"]=='ml':
                        Synth["Qté"]=qte*(Synth["Qté Jour"]+Synth["Qté Nuit"])+1
                    else : 
                        Synth["Qté"]=Synth["Qté Jour"]+Synth["Qté Nuit"]
                    Synth["Total Fourniture"]=float(Synth["Fourniture P.U. (€)"])*Synth["Qté"]
                    Synth["Total MO"]=(float(Synth["Qté Jour"])*float(Synth["M.O Jour P.U. (€)"]))+(float(Synth["Qté Nuit"])*float(Synth["M.O Nuit P.U. (€)"]))
                    Synth["Montant Total en €"]=float(Synth["Total MO"])+float(Synth["Total Fourniture"])
                    Synth["Sous Systeme"]=dataQT.loc[i,'Ssysteme']
                    somme1=somme1+Synth["Total Fourniture"]
                    somme2=somme2+Synth["Total MO"]
                    des=dataQT.loc[i,'Prestations']
                    
                    d.append(Synth)
        data_init.ll.append(d)
        my_dict={"Désignation":des ,"Total Fourniture":somme1,"Total MO":somme2}
        data_init.liste.append(my_dict)
    flat_list = [item for sublist in data_init.ll for item in sublist]
    #flat_list_resume = [item for sublist in data_init.liste for item in sublist]
    d=(pd.DataFrame(flat_list))
    d.to_excel("estimation.xlsx")
    test = (d).astype(str)
    st.dataframe(test)
    dd=(pd.DataFrame(data_init.liste))
    if st.button('Consulter calcul par sous prestation'):
            dd=(pd.DataFrame(data_init.liste))
            dd.to_excel("Resume.xlsx")
            testt = (dd).astype(str)
            st.dataframe(testt)
    else :
        pass
    return d , dd
def get_dataframe(df):
            d=[]
            for  ss in df['Sous Systeme'].unique():
                    
                    dictionnaire=dict()
                    dd=df[(df['Sous Systeme']==ss) ]
                    s1=dd['Total Fourniture'].sum()
                    s2=dd['Total MO'].sum()
                    dictionnaire['Sous Systeme']=ss
                    dictionnaire['Total Fourniture']=s1
                    dictionnaire['Total MO']=s2
                    d.append(dictionnaire)
            gf=pd.DataFrame(d)
            
            return gf
            
def calcul_total(dataQT,data):
    df,dd=estimation(dataQT,data)
    df['Total Fourniture'].astype(float)
    df['Total MO'].astype(float)
    dd['Total Fourniture'].astype(float)
    dd['Total MO'].astype(float)
    if st.button('Consulter calcul par sous systeme'):
            d=dict()
            for  ss in df['Sous Systeme'].unique():
                    dictionnaire=dict()
                    dd=df[(df['Sous Systeme']==ss) ]
                    s1=dd['Total Fourniture'].sum()
                    s2=dd['Total MO'].sum()
                    dictionnaire['Total Fourniture']=s1
                    dictionnaire['Total MO']=s2
                    d[ss]=dictionnaire
            gf=pd.DataFrame(d)
            testt = (gf).astype(str)
            st.dataframe(testt)
            
            
    elif st.button('Visualisation'):
         
                gf=get_dataframe(df)
                fig = px.bar(dd, x = "Désignation",y = "Total Fourniture",title = "Cout Fourniture par prestation" )
                st.plotly_chart(fig)
                fig = px.bar(dd, x = "Désignation",y = "Total MO",title = "Cout MO par prestation" )
                st.plotly_chart(fig)
            
                fig = px.bar(gf, x = "Sous Systeme",y = "Total Fourniture",title = "Cout Fourniture par sous systeme" )
                st.plotly_chart(fig)
                fig = px.bar(gf, x = "Sous Systeme",y = "Total MO",title = "Cout MO par sous systeme" )
                st.plotly_chart(fig)    
            
    else:
            pass 
    
    