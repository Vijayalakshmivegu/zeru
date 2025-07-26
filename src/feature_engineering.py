
import pandas as pd
import numpy as np
import os
import os

if not os.path.getsize('output/compound_v2_transactions.csv'):
    print("No transaction data found. Exiting.")
    exit()

def extract_features(transactions_csv):
    # Exit if the input CSV is empty
    if not os.path.getsize(transactions_csv):
        print("No transaction data found. Exiting.")
        exit()
    """
    Given a CSV of Compound transactions, extract features for each wallet.
    Returns a DataFrame with one row per wallet and feature columns.
    """
    try:
        df = pd.read_csv(transactions_csv)
    except pd.errors.EmptyDataError:
        print("Transaction CSV is empty or invalid. Exiting.")
        exit()
    features = []
    for wallet, group in df.groupby('wallet'):
        feature = {}
        feature['wallet'] = wallet
        feature['num_transactions'] = len(group)
        feature['unique_tokens'] = group['tokenSymbol'].nunique() if 'tokenSymbol' in group else 0
        feature['total_value'] = group['value'].astype(float).sum() if 'value' in group else 0
        feature['first_tx_time'] = pd.to_datetime(group['timeStamp'], unit='s').min() if 'timeStamp' in group else np.nan
        feature['last_tx_time'] = pd.to_datetime(group['timeStamp'], unit='s').max() if 'timeStamp' in group else np.nan
        feature['active_days'] = (feature['last_tx_time'] - feature['first_tx_time']).days if pd.notnull(feature['first_tx_time']) and pd.notnull(feature['last_tx_time']) else 0
        # Add more features as needed
        features.append(feature)
    features_df = pd.DataFrame(features)
    return features_df

def save_features(features_df, output_path):
    features_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Example usage
    features_df = extract_features('output/compound_v2_transactions.csv')
    save_features(features_df, 'output/wallet_features.csv')
    print("Feature extraction complete.")
