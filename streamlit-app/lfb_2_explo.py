# Core Pkg
import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def exploration():
    with st.container():
        st.title("Exploration🕵️‍♂️")
        
                
   
    #Import des datafames
    @st.cache
    def load_data(url):
        df = pd.read_csv(url)
        return df
    
    df_mob = load_data("data_mob_2021.csv")
    df_inc = load_data("data_inc_2021.csv")
    df_summary = load_data("data_summary.csv")

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
    st.write("Il y a", df.shape[0], "lignes et", df.shape[1], "colonnes dans le jeu de données fusionnées")

    #Summary
    st.header("Résumé")
    st.dataframe(df_summary, use_container_width = True)
"""
    @st.cache_data
    def summarize(df):
        table = pd.DataFrame(index=df.columns, columns=['type_info', 'nb_NaN', '%_NaN', 'nb_unique_values', 'list_unique_values', 'dup', "mean_or_mode", "min", "max", "flag"])
        table.loc[:, 'type_info'] = df.dtypes.values
        table.loc[:, 'nb_NaN'] = df.isna().sum().values
        table.loc[:, '%_NaN'] = df.isna().sum().values / len(df)
        table.loc[:, 'nb_unique_values'] = df.nunique().values
        table.loc[:, 'dup'] = df.duplicated().sum()

        def get_list_unique_values(colonne):
            if colonne.nunique() < 6:
                    return colonne.unique()
            else:
                    return "Too many categories..." if colonne.dtypes == "O" else "Too many values..."

        def get_mean_mode(colonne):
            return colonne.mode()[0] if colonne.dtypes == "O" else colonne.mean()

        def alerts(colonne, thresh_na = 0.25, thresh_balance = 0.8):
            if (colonne.isna().sum()/len(df)) > thresh_na:
                return "Too many missing values ! "
            elif colonne.value_counts(normalize=True).values[0] > thresh_balance:
                return "It's imbalanced !"
            else:
                return "Nothing to report"

        table.loc[:, 'list_unique_values'] = df.apply(get_list_unique_values)
        table.loc[:, 'mean_or_mode'] = df.apply(get_mean_mode)
        table.loc[:, 'min'] = df.min() # Affichage de la plus petite valeur
        table.loc[:, 'max'] = df.max() # Affichage de la plus grande valeur
        table.loc[:, 'flag'] = df.apply(alerts)

        return table

    summary = summarize(df)


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
    """