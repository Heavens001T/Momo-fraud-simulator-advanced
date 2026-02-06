import pandas as pd
import random
from constants import TX_TYPES, USER_PROFILES

def generate_transaction():
    """
    Generates a random simulated transaction
    """
    tx = {
        "amount": random.randint(500, 500_000),
        "hour": random.randint(0,23),
        "transactions_last_hour": random.randint(1,20),
        "new_device": random.randint(0,1),
        "location": random.choice(["Yaoundé","Douala","Bamenda","Garoua","Limbe"]),
        "tx_type": random.choice(TX_TYPES),
        "user_profile": random.choice(USER_PROFILES)
    }
    return pd.DataFrame([tx])
