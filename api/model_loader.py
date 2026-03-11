import pickle

def load_model():
    with open("C:/Users/JAYARAM/Desktop/TrafficIQ/ml_model/model.pkl", "rb") as f:
        model = pickle.load(f)
    return model