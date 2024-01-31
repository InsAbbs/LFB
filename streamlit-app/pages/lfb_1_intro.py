# Core Pkg
import streamlit as st

def intro():
    st.title("La Bridage des Pompiers de Londres")

    st.markdown(
        """
        La Brigade des Pompiers de Londres est le service d'incendie et de sauvetage le plus actif du Royaume-Uni et l'une des plus grandes organisations de lutte contre les incendies et de sauvetage au monde. La London Fire Brigade (LFB) met à disposition sur son site officiel les données relatives aux incidents enregistrés depuis janvier 2009, ainsi que les informations concernant les camions de pompiers envoyés sur les lieux des incidents. Ce rapport est basé sur l’exploration et le traitement de ces données dans le but d’analyser et d’estimer le temps de réaction de la LFB.
        
        L’objectif de ce projet est d’analyser et estimer les temps de réponse et de mobilisation de la Brigade des Pompiers de Londres. 

        **👈 Naviguez vers les étapes d'exploration, visualisation, pré-processing, et modélisation du projet.**""")
    
    _left, _right = st.columns(2)
    with _left:
        st.video(data = "https://www.youtube.com/watch?v=QkKr77M_BlE")
    with _right:
        st.markdown(
            """
            ### Sources
            - [London Datastore](https://data.london.gov.uk/)
            - [London Fire Brigade Incident Records](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)
            - [London Fire Brigade Mobilisation Records](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records)
            - [Incident Recording System – Questions and Lists](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/974650/incident-recording-system-questions-and-lists-version-1.6-XML-Schemas-v1-0p-from-April-2012.pdf)
            """
    )
