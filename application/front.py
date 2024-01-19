import streamlit as st 
import base64


# =============================================================>

# CSS du formuaire. 
def formulaire_css():
    css="""
    <style>
        [data-testid="column"] {
            background: #2c3a41;
            box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
            border-radius: 10px;
            padding: 5%;
            
            /* Ajout des styles pour le centrage */
            display: flex;
            # justify-content: center;
            # align-items: center;
            transition: background-color 0.3s ease; 
        }
        
        [data-testid="column"]:hover {
                background-color: #3a4d57; /* Nouvelle couleur de fond au survol */
                cursor: pointer; /* Curseur de la main pour indiquer la cliquabilité */
            }
    </style>
    """
    st.write(css, unsafe_allow_html=True)

# =============================================================>

# Fonction pour charger une image.
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =============================================================>

# Fonction pour mettre une image en background.
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
# =============================================================>

# Fonction pour ajouter du CSS au bouton.
def button_css():
    st.markdown(
        """
        <style>
            .stButton>button {
                font-weight: bold;
                background-color: #f47a5c; 
                color: white; 
                padding: 10px 20px; 
                margin-left:213px;
                border-radius: 5px; 
                width: 275px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Utiliser les boutons personnalisés
    button2_clicked = st.button("**Estimer mon bien**", key="button2")
    return button2_clicked

# =============================================================>

# Fonction permettent d'afficher la prédictions
def css_predictions(prediction):
    st.markdown(
        """
        <style>
            .custom-block {
                background-color: #2c3a41; 
                color: white; 
                padding: 20px; 
                border-radius: 10px; 
                width: 700px; 
                height: 150px;
                display: flex; 
                justify-content: center; 
                align-items: center; 
                font-size: 60px;
                box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);  
                transition: background-color 0.3s ease; 
            }
            .custom-block:hover {
                background-color: #3a4d57; 
                cursor: pointer; 
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='custom-block'>{prediction}</div>", unsafe_allow_html=True)

# =============================================================>

# Permet d'apporter du CSS au texte/titre.
def css_texte(color:str, size:str, texte:str):
    new_title  = f'<h1 style="color:{color}; font-size: {size}; text-align:center">{texte}</h1>'
    st.markdown(new_title, unsafe_allow_html=True)
        
# =============================================================>

# Permet de charger le CSS dans le streamlit.
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
# =============================================================>
