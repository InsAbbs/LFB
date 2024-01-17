# Core Pkg
import streamlit as st
import pandas as pd

@st.cache_data
def exploration():
    with st.container():
        st.title("Exploration🕵️‍♂️")
                
    #Import des datafames
    @st.cache_data
    def load_data(url):
        df = pd.read_csv(url)
        return df
    
    df_mob = load_data("LFB\streamlit-app\data\data_mob_2021.csv")
    df_inc = load_data("LFB\streamlit-app\data\data_inc_2021.csv")
    summary = load_data("LFB\streamlit-app\data\summary.csv")
    
    @st.cache_data
    def merge(df1, df2):
        df3 = df1.merge(right=df2, on = ["IncidentNumber", "CalYear", "HourOfCall"], how = "left")
        return df3
    
    df = merge(df_mob, df_inc)
    
    st.header("Rapport des incidents")
    st.dataframe(df_inc.head())
    st.write("Il y a", df_inc.shape[0], "lignes et", df_inc.shape[1], "colonnes dans le rapport des Incidents")

    st.header("Rapport des mobilisations")
    st.dataframe(df_mob.head())
    st.write("Il y a", df_mob.shape[0], "lignes et", df_mob.shape[1], "colonnes dans le rapport des Mobilisations")
    
    #Merge
    st.header("Merge")
    st.dataframe(df.head(), use_container_width = True)

    #Description des rapports 'Incident' et 'Mobilisation' après fusion
    st.write("Il y a", df.shape[0], "lignes et", df.shape[1], "colonnes dans le jeu de données fusionnées")

    #Résumé
    st.header("Résumé")
    st.write("Exploration du dataframe avec la fonction personnalisée 'summary'")
    summary.rename(columns={summary.columns[0]: 'Variable'},inplace=True)
    st.dataframe(summary)

    #Tests statistiques
    from scipy.stats import chi2_contingency
    st.header("Test de khi2 sur les variables 'PropertyCategory' et 'IncidentGroup'")
    st.subheader("")
    st.write("Hypothèses")
    st.write("#H0 : la variable de catégorie d'incident est indépendante du type d'incident")
    st.write("#H1 : la variable de catégorie d'incident n'est pas indépendante du type d'incident")
    contingency_table = pd.crosstab(df['PropertyCategory'], df['IncidentGroup'])
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    st.write("Résultats du test du chi2 :")
    st.write("Valeur du chi2 :", chi2)
    st.write("p-value :", p_value)
    st.write("Degrés de liberté :", dof)
    st.success("Conclusion : p-val très petite (< 0.05) => on rejette H0 et on accepte H1.")

    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    st.subheader("Test ANOVA sur les variables 'IncidentGroup' et 'TurnoutTimeSeconds'")
    result = smf.ols('TurnoutTimeSeconds ~ IncidentGroup', data=df).fit()
    table = sm.stats.anova_lm(result)
    st.write("Tableau ANOVA :")
    st.dataframe(table)