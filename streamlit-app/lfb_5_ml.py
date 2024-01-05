# Core Pkg
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


@st.cache_data(experimental_allow_widgets=True)
def machine():
    st.title("Modélisation 🪄")

    st.subheader("Apprentissage supervisé --- Régression")

    #Import des dataframes
    @st.cache_data
    def load_data(url):
        df = pd.read_csv(url, index_col = 0)
        return df
    
    stats = load_data("data/statistiques.csv")
    optimisation = load_data("data/optimisation.csv")
    df = load_data("data/modelisation.csv")
    df = df[(df.YearOfCall == 2023) & (df.MonthOfCall == 1)]
    stats = stats.sort_values(by = "Modèle")
    stats_2016 = stats[stats["sample"] == "2016-2023"]
    stats_2022 = stats[stats["sample"] == "2022-2023"]
    stats_2023 = stats[stats["sample"] == "2023"]
    stats_2016 = stats_2016.drop(["Score sur test", "sample"], axis = 1)
    stats_2022 = stats_2022.drop(["Score sur test", "sample"], axis = 1)
    stats_2023 = stats_2023.drop(["Score sur test", "sample"], axis = 1)
    
    st.markdown("""
        - Séparation des variables **explicatives** de la **variable cible**""")
    with st.echo():
        feats = df.drop('ReactionTime', axis=1)
        target = df['ReactionTime']
    
    st.markdown("""
        - **Hold-out** : train_test_split""")                  
    with st.echo():
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(feats, target, test_size=0.2, random_state=42)     
    
    st.markdown("""
        - **Métriques**""")
    with st.echo():
                 from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
                  
    st.markdown("""
            * **Transformations**
                * **StandardScaler()**  pour la normalisation des variables quantitatives
                * **LabelEncoder()**    pour la transformation des variables qualitatives""")


    with st.echo():
        from sklearn.preprocessing import LabelEncoder, StandardScaler

                     
    X = df.drop('ReactionTime', axis=1)
    cat_cols = X.select_dtypes(include=['object']).columns
    label_encoder = LabelEncoder()
    X[cat_cols] = X[cat_cols].apply(label_encoder.fit_transform)
    num_cols = X.select_dtypes(include=['int64']).columns
    scaler = StandardScaler()
    X[num_cols] = scaler.fit_transform(X[num_cols])

    st.divider()

    st.subheader("Quels modèles ?")

    with st.echo():
         from sklearn.linear_model import LinearRegression
         from sklearn.linear_model import Ridge
         from sklearn.linear_model import Lasso
         from sklearn.linear_model import ElasticNet
         from sklearn.tree import DecisionTreeRegressor
         from sklearn.ensemble import RandomForestRegressor
         from sklearn.neighbors import KNeighborsRegressor
         from sklearn.neural_network import MLPRegressor

    st.divider()

    st.subheader("Entrainements et scores")
    expander = st.expander("Dataset complet")
    expander.dataframe(stats_2016, use_container_width = True, hide_index = True)
    expander = st.expander("Dataset - échantillon 2022-2023")
    expander.dataframe(stats_2022, use_container_width = True, hide_index = True)
    expander = st.expander("Dataset - échantillon 2023")
    expander.dataframe(stats_2023, use_container_width = True, hide_index = True)

    st.divider()

    st.subheader("Optimisation")

    with st.echo():
         from sklearn.model_selection import GridSearchCV
         grid = {'n_estimators': [50, 100, 150], 'max_depth' : [None, 3, 5, 7]}
         grid_search = GridSearchCV(estimator = RandomForestRegressor(), param_grid = grid)
    st.text("grid_search.best_params_\n"
            ">>> {'n_estimators': 150, 'max_depth': None}")


    st.divider()

    st.subheader("Modulation de n_estimators")
    st.markdown("Scores de RandomForestRegressor")
    stats_rfr = stats[stats["Modèle"] == "RandomForestRegressor"]
    stats_rfr["sample"] = [977708, 220338, 41964]
    stats_rfr = stats_rfr.drop("Score sur test", axis =1)
    st.dataframe(stats_rfr, use_container_width = True, hide_index = True)
    optimisation["sample"] = 220.338
    optimisation = optimisation.rename(columns={"Temps": "Temps d'entrainement"})
    optimisation['Estimateurs'] = 'n_estimators = ' + optimisation['Estimateurs'].astype(str)
    st.dataframe(optimisation, use_container_width = True, hide_index = True)