import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv("C:/Users/JAYARAM/Desktop/TrafficIQ/data/processed/processed_traffic_dataset.csv")

X=df.drop("Vehicles",axis=1)
y=df["Vehicles"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

def get_data():
    return X_train,X_test,y_train,y_test

