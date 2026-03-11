import pickle
import pandas as pd

# Load trained model
with open("C:/Users/JAYARAM/Desktop/TrafficIQ/ml_model/model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_traffic(data: dict):
    """
    Predict traffic volume based on input features
    """

    # Convert input dictionary into DataFrame
    input_df = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(input_df)

    return prediction[0]


# Test prediction if file is run directly
if __name__ == "__main__":
    
    sample_data = {
        "Junction": 2,
        "Year": 2016,
        "Month": 5,
        "Day": 12,
        "Hour": 8,
        "Dayofweek": 3
    }

    result = predict_traffic(sample_data)

    print("Predicted Traffic Volume:", result)