# Core Pkg
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


@st.cache_data
def visu():
    st.title("Visualisation 🎨")

    #Import des dataframes
    @st.cache_data
    def load_data(url):
        df = pd.read_csv(url, sep = ",", header = 0)
        return df
    
    df_mob = load_data("data/data_mob_2021.csv")
    df_inc = load_data("data/data_inc_2021.csv")
    df = load_data("data/data_all_2021.csv")
    
    @st.cache_data
    def merging(df1, df2):
        df3 = df1.merge(right=df2, on = ["IncidentNumber", "CalYear", "HourOfCall"], how = "left")
        return df3
    
    #Graphiques
    st.subheader("Part d'incidents rapportés")
    labels = ['False Alarm', 'Special Service', 'Fire']
    values = df['IncidentGroup'].value_counts()
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

    st.subheader("Répartition des types d'incidents par an")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig, ax = plt.subplots()
    plt.figure(figsize=(15, 6))
    sns.countplot(x="CalYear", hue="IncidentGroup", data=df_inc)
    st.pyplot()

    st.subheader("Répartition des appels en fonction de l'heure")
    sns.countplot(data=df_inc, x="HourOfCall")
    plt.xlabel('Heure')
    plt.ylabel("Nombre d'appels")
    plt.title("Répartition des appels en fonction de l'heure")
    st.pyplot()

    #Matrice de corrélation
    #Définition d'un DF avec seulement les variables numériques
    df_num = df.select_dtypes(include=['int64', 'float64'])
    #Affichage Heatmap
    st.subheader("Heatmap : corrélation entre les valeurs numériques")
    fig, ax = plt.subplots(figsize=(17, 17))
    corr_matrix = df_num.corr().round(2)
    sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt='.2f')
    st.pyplot()