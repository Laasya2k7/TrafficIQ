import pandas as pd


def prepare_input(data: dict):
    """
    Convert input dictionary into a properly formatted DataFrame
    for model prediction.
    """

    df = pd.DataFrame([data])

    # Ensure column order matches training data
    columns = [
        "Junction",
        "Year",
        "Month",
        "Day",
        "Hour",
        "Dayofweek"
    ]

    df = df[columns]

    return df


def validate_input(data: dict):
    """
    Basic validation for input values.
    """

    if data["Month"] < 1 or data["Month"] > 12:
        raise ValueError("Month must be between 1 and 12")

    if data["Hour"] < 0 or data["Hour"] > 23:
        raise ValueError("Hour must be between 0 and 23")

    if data["Dayofweek"] < 0 or data["Dayofweek"] > 6:
        raise ValueError("Dayofweek must be between 0 and 6")

    return True


def format_prediction(prediction):
    """
    Convert model prediction into a clean output format.
    """

    return {
        "predicted_traffic_volume": float(prediction)
    }