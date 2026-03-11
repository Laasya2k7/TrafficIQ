import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from preprocessing import get_data

X_train,X_test,y_train,y_test=get_data()

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

prediction=model.predict(X_test)

mae=mean_absolute_error(y_test,prediction)
r2=r2_score(y_test,prediction)

print("Model Evaluation")
print("----------------")
print("MAE:", mae)
print("R2 Score:", r2)

with open("C:/Users/JAYARAM/Desktop/TrafficIQ/ml_model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
