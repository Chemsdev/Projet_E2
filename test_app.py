# test_app.py
import streamlit as st
import app  

def test_square_number():
    assert app.square_number(2) == 4
    assert app.square_number(0) == 0
    assert app.square_number(-3) == 9





# def test_main():
    
#     # On utilise st.beta_container pour simuler l'environnement Streamlit.
#     with st.beta_container():
        
#         # Simulation utilisteur streamlit.
#         with st.form("Test Form"):
#             input_number = st.number_input("Entrez un nombre :", value=5)
#             submit_button = st.form_submit_button("Calculer le carré")

#         # Vérifiez que l'application renvoie les bons types de données.
#         assert isinstance(input_number, (int, float))
#         assert isinstance(submit_button, bool)
