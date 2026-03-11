from fastapi import FastAPI
import pandas as pd

from api.schemas import TrafficInput
from api.model_loader import load_model

app = FastAPI()

model = load_model()


@app.get("/")
def home():
    return {"message": "Traffic Congestion Prediction API"}


@app.post("/predict")
def predict(data: TrafficInput):

    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)

    return {"predicted_traffic": float(prediction[0])}