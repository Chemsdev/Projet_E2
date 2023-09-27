import streamlit as st 
from utils import *

def square_number(number):
    return number ** 2

def main():
    
    background_front(url="")
    
    st.title("Silicon Valley")
    number = st.text_input("veuillez saisir un nombre ", key=1)
    if st.button("Calculer le carré"):
        result = square_number(int(number))
        st.write(f"Le carré de {number} est {result}")            
main()



