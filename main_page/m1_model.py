import os
import pickle


def load_model():
    file_path = os.path.join(os.path.dirname(__file__), 'rfr_model_34_finale.pkl')

    with open(file_path, 'rb') as file:
        model = pickle.load(file)

    return model
