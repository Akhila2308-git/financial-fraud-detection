import pandas as pd
import os

print("Loading data...")

# Get project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(BASE_DIR, "data", "transactions.csv")

df = pd.read_csv(file_path)

df = df.dropna()

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['hour'] = df['Timestamp'].dt.hour

df['Amount'] = (df['Amount'] - df['Amount'].mean()) / df['Amount'].std()

output_path = os.path.join(BASE_DIR, "data", "cleaned_transactions.csv")

df.to_csv(output_path, index=False)

print("Data Preprocessing Completed")