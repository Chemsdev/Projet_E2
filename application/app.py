import streamlit as st 
from front     import *
from modelling import * 
from api       import * 



def main():
    
    # ========================HOME=============================>
    set_background("image/background.jpg")
    local_css("style.css")
    css_texte(color="#3a4d57", size="45px", texte="Prédictions de prix immobiliers en Californie")
    css_texte(color="#f47a5c", size="25px", texte="Estimez le prix de votre bien !")
    # ========================================================>
    
    
    # =======================Formulaire========================>
    end_formulaire = False
    user_inputs=[]
    formulaire_css()       
    col1, col2, col3 = st.columns(3)
    
    with col1:      
        # Formulaire partie 1.  
        css_texte(color="#f47a5c", size="20px", texte="Logement")
        total_bedrooms     = st.number_input("**Nombre de chambres**", key=1, min_value=1)
        total_rooms        = st.number_input("**Nombre de pièces**", key=2, min_value=1)
        housing_median_age = st.number_input("**Age médian**", key=6, min_value=1)
                
    with col2:        
        # Formulaire partie 3.  
        css_texte(color="#f47a5c", size="20px", texte="Démographie")
        households    = st.number_input("**Nombre de ménages dans un bloc**", key=4, min_value=1)
        median_income = st.number_input("**Revenu médian des ménages dans un bloc**", key=5, min_value=1)
        population    = st.number_input("**Nombre de populations dans un bloc**", key=3, min_value=1)

    with col3:
        # Formulaire partie 2.
        css_texte(color="#f47a5c", size="20px", texte="Localisation")
        options         = ["a 1h de l'océan","loin de la mer","Dans une ile", "près de la baie", "près de l'océan"]
        ville           = st.selectbox("**Ville**", (CHOICE_CITY),   key=8)
        ocean_proximity = st.selectbox("**Proximité océan**",(options), key=9)  
    # ========================================================>
    
    
    # ===============Vérification formulaire==================>
    if button_css():
        
        # Récupération de longitude et de la latitude de la ville choisis.
        longitude, latitude = fetch_data_city_locality(city=ville)
        
        # On enregistre les features dans une liste.
        user_inputs.extend([
            longitude, 
            latitude, 
            housing_median_age, 
            total_rooms,
            total_bedrooms, 
            population, 
            households, 
            median_income,
            ocean_proximity
        ])        
        
        # On vérifie si tout les éléments ont bien été saisit.
        if check_form(user_inputs):
            end_formulaire = True
        else:
            css_texte(color="#3a4d57", size="20px", texte="Veuillez remplir tout le formulaire !")
    # ========================================================>
    
    
    # ====================Prédiction==========================>
    # Le formulaire à bien été rempli.
    if end_formulaire:     
        # Préparation des features et exécution du modèle.
        features_model = traitement_features(values_features=user_inputs.copy())
        new_prediction = model.predict(features_model)
          
        # Affichage de la prédiction
        css_texte(color="#f47a5c", size="30px", texte="Valeur de votre bien")
        css_predictions(f"{round(int(new_prediction[0]))} $")
        
        # Récapitulatif (Amélioration)
        css_recapitulatif(user_inputs=user_inputs, prediction=round(int(new_prediction[0])))
    # ========================================================>




main()



