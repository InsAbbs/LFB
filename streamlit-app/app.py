# Core Pkg
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
# Custom modules
from lfb_1_intro import intro # Basic streamlit function
from lfb_2_explo import exploration # Basic streamlit function
from lfb_3_visu import visu # Basic streamlit function
from lfb_4_npp import nettoyage # Basic ML web app with stremlit
from lfb_5_ml import machine # Basic ML web app with stremlit
from lfb_7_bonus import bonus # Basic ML web app with stremlit

import os

st.set_page_config(
    page_title="London Fire Brigade",
    page_icon="fire-engine",
    layout = "wide")

def main():
    # List of pages
    liste_menu = ["Introduction", "Exploration", "Visualisation", "Pré-processing", "Modélisation"]

    # Sidebar
    logo = "https://upload.wikimedia.org/wikipedia/en/thumb/9/92/London_Fire_Brigade_logo.svg/2560px-London_Fire_Brigade_logo.svg.png"
    st.sidebar.image(logo, use_column_width=True)
    with st.sidebar:
        selected = option_menu("Menu", liste_menu,
        icons=['card-list', 'zoom-in', 'palette', 'tools', 'database-fill-gear'], menu_icon="fire", default_index=0)

    # Page navigation
    if selected == 'Introduction':
        intro()
    if selected == 'Exploration':
        exploration()
    if selected == 'Visualisation':
        visu()
    if selected == 'Pré-processing':
        nettoyage()
    if selected == 'Modélisation':
        machine()


if __name__ == '__main__':
    main()