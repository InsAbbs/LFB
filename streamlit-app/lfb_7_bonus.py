# Core Pkg
import pandas as pd
import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder


# Custom function
# st.cache is used to load the function into memory
@st.cache_resource
def train_model(model_choisi, X_train, y_train, X_test, y_test) :
    if model_choisi == 'RandomForestRegression_Basic':
        model = RandomForestRegressor()
    if model_choisi == 'RandomForestRegression_Grid':
        model = RandomForestRegressor(n_estimators=800,
                                max_features='sqrt',
                                max_depth=None,
                                random_state=42)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    return np.round(score, 4)

def bonus():
    ### Create Title
    st.image('https://media.tenor.com/K8AdV_HpdZ4AAAAi/tegan-teganiversen.gif', width = 200)
    st.header("999, what's your encoder ?")

    @st.cache_data
    def load_data(url):
        df = pd.read_csv(url)
        return df
    df = load_data("data/LFB_Modelisation_v3.csv")
    df = df[(df.YearOfCall == 2022) & (df.MonthOfCall <= 6)]


    ### Transforming the data
    y = df['ReactionTime']
    X = df.drop('ReactionTime', axis=1)
    cat_cols = X.select_dtypes(include=['object']).columns
    num_cols = X.select_dtypes(include=['int64']).columns
    scaler = StandardScaler()
    X_num = X[num_cols]
    X[num_cols] = scaler.fit_transform(X[num_cols])
    ohe = OneHotEncoder(drop = "first", sparse = False)
    X_cat = pd.DataFrame(ohe.fit_transform(X[cat_cols]), columns = ohe.get_feature_names_out(cat_cols))
    X_num.reset_index(drop=True, inplace=True)
    X_cat.reset_index(drop=True, inplace=True)
    X = X_cat.join(X_num)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #  Baseline model
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Other models
    model_list = ['RandomForestRegression_Basic', 'RandomForestRegression_Grid']
    model_choisi = st.selectbox(label = "Select a model" , options = model_list)


    # Showing the accuracy for the orthers models (for comparison)
    st.write("Score", train_model(model_choisi, X_train, y_train, X_test, y_test))