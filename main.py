from models.predict import predict_transaction
from alert_system.alert import send_alert
import pandas as pd
import os

print("Running Fraud Detection...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "data", "final_features.csv")

df = pd.read_csv(data_path)

# Remove Timestamp for prediction
df = df.drop(columns=["Timestamp"])

for i in range(len(df)):
    transaction = df.drop("Is_Fraud", axis=1).iloc[i].values
    result = predict_transaction(transaction)

    if result == 1:
        send_alert(df.iloc[i])