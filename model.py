import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    np.random.seed(42)
    data = pd.DataFrame({
        "amount": np.random.randint(500, 500_000, 500),
        "hour": np.random.randint(0, 24, 500),
        "transactions_last_hour": np.random.randint(1, 20, 500),
        "new_device": np.random.randint(0, 2, 500)
    })
    # Simple fraud label for demo
    data["fraud"] = ((data["amount"] > 150000) & (data["transactions_last_hour"] > 5) & (data["new_device"] == 1)).astype(int)
    X = data.drop("fraud", axis=1)
    y = data["fraud"]
    model = RandomForestClassifier()
    model.fit(X, y)
    return model, X.columns

def predict_transaction(model, input_df):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    return prediction, probability
