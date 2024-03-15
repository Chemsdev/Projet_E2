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
    button2_clicked = st.button("**Estimé mon bien**", key="button2")
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

# Fonction permettent d'afficher la prédictions
def css_recapitulatif(user_inputs, prediction):
    
    name_input = [
        "longitude", 
        "latitude", 
        "Age médian", 
        "Nombre de pièces",
        "Nombre de chambres", 
        "Nombre de populations dans un bloc", 
        "Nombre de ménages dans un bloc", 
        "Revenu médian",
        "Proximité océan"
    ]

    st.markdown(
        """
        <style>
            .custom-block2 {
                background-color: #2c3a41; 
                color: white; 

              
                border-radius: 10px; 

                padding: 15px; 
                
                justify-content: center; 
                align-items: center; 
                
            
                font-weight: bold;
                width: 410px; 
                height: 400px;
                margin-left:155px;
                margin-top: 80px;
                font-size: 18px;
                transition: background-color 0.3s ease; 
            }
            .custom-block2:hover {
                background-color: #2c3a41; 
                cursor: pointer; 
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class='custom-block2'>
           <h3 style="color:#f47a5c";"text-align:center";> Récapitulatif de votre bien </h1>
            {'<br>'.join([f'{i} : <span style=color:#f4ddb1;font-size:21px;>{j} </span>' for (i, j) in zip(name_input, user_inputs)])}
            <p></p>
        </div>
        """,
        unsafe_allow_html=True
    )