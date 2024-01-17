import streamlit as st
import pandas as pd

#Import des dataframes
def load_data(url):
    df = pd.read_csv(url, sep=';', header=0)
    return df

def nettoyage():  # sourcery skip: extract-duplicate-method, inline-variable

    #Titre
    st.title("Pré-processing 🛠️")

    #Sous titre
    st.header("Pertinence des variables")

    #Texte
    st.write("Avec le volume de notre jeu de données, cette étape est importante pour la suite\ndu projet et l'entrainement des modèles qui nous attend.")

    #Subheader 1
    st.subheader('Trois principales catégories de données :')
    _left, _mid, _right = st.columns(3)
    with _left:
        imgmap = "https://images.unsplash.com/photo-1619468129361-605ebea04b44?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80"
        st.image(imgmap, width = 300, caption = "Géographiques")
    with _mid:
        imgtime = "https://images.unsplash.com/photo-1508962914676-134849a727f0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
        st.image(imgtime, width = 300, caption = "Temporelles")
    with _right:
        imgmetier = "https://southwarknews.co.uk/wp-content/uploads/2021/10/stock-logo-ppe-1-london-fire-brigade.jpg"
        st.image(imgmetier, width = 300, caption = "Métier")

    #Choix
    st.info("A noter : Nous avons fait le choix de retenir au moins une variable de chacun des trois grands groupes de données dans l'idée de ne pas trop appauvrir notre modèle de prédiction")

    #Subheader 2
    st.subheader("Définition de la variable cible")
    st.success("ReactionTime = MobilisationTime + TravelTimeSeconds\n\nNotre variable cible est donc un nombre entier qui correspond à un temps en secondes")

    #Subheader 3
    st.subheader("Création de nouvelles variables")
    created_col = load_data("data/created_col.csv")
    st.dataframe(created_col, use_container_width = True)

    #Subheader 4
    st.subheader("Nettoyage du dataset")
    deleted_col = load_data("data/deleted_col.csv")
    st.dataframe(deleted_col, use_container_width = True)

    #Subheader 5
    st.subheader("Dataset final")
    dataset_final = load_data("data/dataset_final.csv")
    st.dataframe(dataset_final, use_container_width = True)