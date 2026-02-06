from constants import WEIGHT_AMOUNT, WEIGHT_TX_COUNT, WEIGHT_NEW_DEVICE, WEIGHT_LOCATION, MAX_AMOUNT, MAX_TX_PER_HOUR

def risk_decision(probability):
    if probability < 0.3:
        return "APPROVED", "success"
    elif probability < 0.7:
        return "OTP_REQUIRED", "warning"
    else:
        return "BLOCKED", "error"

def calculate_weighted_risk(tx):
    score = 0
    if tx["amount"].iloc[0] > MAX_AMOUNT:
        score += WEIGHT_AMOUNT
    if tx["transactions_last_hour"].iloc[0] > MAX_TX_PER_HOUR:
        score += WEIGHT_TX_COUNT
    if tx["new_device"].iloc[0] == 1:
        score += WEIGHT_NEW_DEVICE
    if tx["location"].iloc[0] not in ["Yaoundé", "Douala"]:
        score += WEIGHT_LOCATION
    return min(score, 1.0)
