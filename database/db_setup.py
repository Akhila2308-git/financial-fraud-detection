import sqlite3
import pandas as pd
import os

print("Creating Database...")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_path = os.path.join(BASE_DIR, "data", "final_features.csv")
db_path = os.path.join(BASE_DIR, "database", "fraud_detection.db")

conn = sqlite3.connect(db_path)

df = pd.read_csv(input_path)

df.to_sql("transactions", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Database Created Successfully")