import pandas as pd

print("Performing Feature Engineering...")

df = pd.read_csv("data/cleaned_transactions.csv")

# Convert Timestamp to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extract hour
df['hour'] = df['Timestamp'].dt.hour

# Create night transaction feature
df['is_night'] = df['hour'].apply(lambda x: 1 if x < 6 else 0)

# Convert categorical columns to numbers
df['Location'] = df['Location'].astype('category').cat.codes
df['Device'] = df['Device'].astype('category').cat.codes

# REMOVE Timestamp column (important)
df = df.drop(columns=['Timestamp'])

df.to_csv("data/final_features.csv", index=False)

print("Feature Engineering Completed")