import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pickle



# =================================================================>

# Vérification si les champs du formulaire sont remplis.
def check_form(liste:list):
    for i in liste:
        if not i:
            return False
    return True

# =================================================================>

# Fonction permettent de traiter les valeurs saisit pour le modèle: mettre en l'ordre les features, traduire proximity ocean...
def traitement_features(values_features):    
    
    # Récupération du dernier élément de la liste (exemple : loin de la mer)
    ocean_proximity_value = values_features.pop()
    proximity_ocean_dict = {
        "a 1h de l'océan":0.0,
        "loin de la mer" :0.0,
        "Dans une ile"   :0.0,
        "près de la baie":0.0,
        "près de l'océan":0.0,
    }     
    
    # On met 1.0 pour la valeur choisit par l'utilisateur.
    proximity_ocean_dict[ocean_proximity_value] = 1.0
        
    # On créer un dictionnaire avec le nom des features et les valeurs saisit. (exemple: longitude : 5)
    name_features = [
        "longitude", 
        "latitude", 
        "housing_median_age", 
        "total_rooms", 
        "total_bedrooms", 
        "population", 
        "households",
        "median_income",
    ]
    data_dict={}
    for (i, j) in zip(name_features, values_features):
        data_dict[i] = int(j)
        
    # On récupère les valeurs du dictionnaire proximity ocean français, pour les mettres dans le dictionnaire anglais.
    proximity_ocean_dict_english = {
        "_<1H OCEAN" :proximity_ocean_dict["a 1h de l'océan"],
        "_INLAND"    :proximity_ocean_dict["loin de la mer"],
        "_ISLAND"    :proximity_ocean_dict["Dans une ile"],
        "_NEAR BAY"  :proximity_ocean_dict["près de la baie"],
        "_NEAR OCEAN":proximity_ocean_dict["près de l'océan"],
    }
    
    # On concatène les 2 dataframes et on créer un dataframe.
    features_data =  {**data_dict, **proximity_ocean_dict_english}
    df = pd.DataFrame([features_data])
    return df

# =================================================================>

# Preprocessing des données.
def preprocessing(imputing:bool):
    # Import de la data
    data = pd.read_csv("data/Housing_Price.csv")
    
    
    # Nettoyage : Encodage, conversion des colonnes.     
    if "gender" in data.columns:
        data.drop("gender", axis=1,inplace=True)
    if "households" in data.columns:
        data['households'].replace("no", np.nan , inplace=True)
        data["households"] = data["households"].astype('float64')
    if "ocean_proximity" in data.columns:
        data = pd.get_dummies(data, columns=['ocean_proximity'], prefix=[""])
    
    # Imputing des données.     
    if imputing:
        knn_imputer = KNNImputer(n_neighbors=2)  
        imputed_data = knn_imputer.fit_transform(data)
        imputed_df = pd.DataFrame(imputed_data, columns=data.columns)
        
        # On retourne le Dataframe avec données manquantes imputées.         
        return imputed_df
    
    # On retourne le Dataframe avec données manquantes non imputées.         
    return data

# =================================================================>

# Charger le modèle depuis le fichier pickle
with open('decision_tree_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
# =================================================================>