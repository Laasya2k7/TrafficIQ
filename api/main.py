from fastapi import FastAPI
import pandas as pd

from api.schemas import TrafficInput
from api.model_loader import load_model
from utils.helpers import prepare_input, validate_input, format_prediction

app = FastAPI()

model = load_model()


@app.get("/")
def home():
    return {"message": "Traffic Congestion Prediction API"}


@app.post("/predict")
def predict(data: TrafficInput):

    input_data = data.dict()

    validate_input(input_data)

    input_df = prepare_input(input_data)

    prediction = model.predict(input_df)

    return format_prediction(prediction[0])