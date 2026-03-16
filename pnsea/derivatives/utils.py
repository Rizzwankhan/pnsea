# pnsea/derivatives/utils.py
import pandas as pd

# Define the required fields to extract for both CE and PE
required_fields = [
    # OI
    "openInterest",
    "changeinOpenInterest",
    "pchangeinOpenInterest",    # % OI change from prev close — replaces CE_OI_chg_pct calc
    # Price
    "lastPrice",
    "change",                   # absolute price change from prev close
    "pchange",                  # % price change from prev close — replaces add_netchange()
    "impliedVolatility",
    # Volume
    "totalTradedVolume",
    "totalBuyQuantity",         # total buy orders
    "totalSellQuantity",        # total sell orders
    # Order Book — Level 1 to 5
    "buyPrice1", "buyQuantity1",
    "buyPrice2", "buyQuantity2",
    "buyPrice3", "buyQuantity3",
    "buyPrice4", "buyQuantity4",
    "buyPrice5", "buyQuantity5",
    "sellPrice1", "sellQuantity1",
    "sellPrice2", "sellQuantity2",
    "sellPrice3", "sellQuantity3",
    "sellPrice4", "sellQuantity4",
    "sellPrice5", "sellQuantity5",
    # Underlying
    "underlyingValue",          # spot price per strike row
]

# Function to extract required fields from a dictionary column
def extract_option_data(option_series):
    extracted_data = []
    for option_dict in option_series:
        if isinstance(option_dict, dict):
            extracted_data.append({key: option_dict.get(key, None) for key in required_fields})
        else:
            extracted_data.append({key: None for key in required_fields})
    return pd.DataFrame(extracted_data)
