import pytest 
import pickle
import pandas as pd


# Les fonctions à tester.
from api       import fetch_data_city_locality
from modelling import traitement_features




# TEST 1 : API OPENWEATHER.
# =========================================================>
@pytest.fixture
def valid_input() -> tuple:
    return ("Los Angeles",)

def test_fetch_data_city_locality(valid_input):
    data = fetch_data_city_locality(*valid_input)
    assert data == (34.0536909, -118.242766)
# =========================================================>


# TEST 2 : IMPORT MODEL PICKLE.
# =========================================================>
@pytest.fixture
def trained_model():
    with open("decision_tree_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def test_load_pickled_model(trained_model):
    assert trained_model is not None
# =========================================================>


# TEST 3 : TRAITEMENT FORMULAIRE.
# =========================================================>
@pytest.fixture
def valid_input_form() -> list:
    user_inputs = [
        34.0536909, 
        -118.242766, 
        34, 
        35,
        36, 
        37, 
        38, 
        39,
        "a 1h de l'océan"
    ]
    return user_inputs

def test_traitement_features(valid_input_form):
    data = traitement_features(valid_input_form)
    assert isinstance(data, pd.DataFrame)
# =========================================================>

