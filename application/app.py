import streamlit as st 
from utils import *


def main():
    
    # Background.
    background_front(url="https://c.wallhere.com/photos/9f/f9/usa_california_city_bridge_bay_fog-1058582.jpg!d")
    
    # Title.
    st.title("Silicon Valley")
    st.header("Prédicitons des prix immobiliers")
    
    # Formulaire.
    features_1 = st.text_input("veuillez saisir... ", key=1)
    features_2 = st.text_input("veuillez saisir...", key=2)
    features_3 = st.text_input("veuillez saisir...", key=3)
    
main()



