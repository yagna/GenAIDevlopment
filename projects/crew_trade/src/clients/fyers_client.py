from fyers_apiv3 import fyersModel
from src.config import FYERS_CLIENT_ID, FYERS_ACCESS_TOKEN

fyers = fyersModel.FyersModel(client_id=FYERS_CLIENT_ID, token=FYERS_ACCESS_TOKEN, log_path="./logs/")

def place_order(symbol: str, side: str, qty: int):
    side_flag = 1 if side.upper() == "BUY" else -1
    data = {
        "symbol": symbol,
        "qty": qty,
        "type": 2,
        "side": side_flag,
        "productType": "INTRADAY",
        "limitPrice": 0,
        "stopPrice": 0,
        "disclosedQty": 0,
        "validity": "DAY",
        "offlineOrder": "False"
    }
    resp = fyers.place_order(data=data)
    return str(resp)
