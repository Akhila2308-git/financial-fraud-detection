import pandas as pd

def predict_transaction(transaction):

    # Convert input to DataFrame
    df = pd.DataFrame([transaction])

    amount = df["Amount"].iloc[0]

    # Simple rule for demo
    if amount >= 10000:
        return 1   # Fraud
    else:
        return 0   # Normal