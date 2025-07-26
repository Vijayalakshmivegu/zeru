import pandas as pd
import numpy as np

def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min()) if series.max() > series.min() else series * 0

def compute_risk_score(features_csv):
    """
    Assign a risk score (0-1000) to each wallet based on features.
    """
    import os
    if not os.path.exists(features_csv):
        print(f"Features file {features_csv} does not exist. Exiting.")
        exit()
    try:
        df = pd.read_csv(features_csv)
    except pd.errors.EmptyDataError:
        print("Features CSV is empty or invalid. Exiting.")
        exit()
    # Example: Higher num_transactions and active_days = lower risk
    # Lower total_value = higher risk
    # You can adjust weights and logic as needed
    df['score_raw'] = (
        0.4 * min_max_normalize(df['num_transactions']) +
        0.3 * min_max_normalize(df['active_days']) -
        0.3 * min_max_normalize(df['total_value'])
    )
    # Normalize to 0-1000
    df['score'] = min_max_normalize(df['score_raw']) * 1000
    df['score'] = df['score'].clip(0, 1000).round().astype(int)
    return df[['wallet', 'score']]

def save_scores(scores_df, output_path):
    scores_df.to_csv(output_path, index=False, header=['wallet_id', 'score'])

if __name__ == "__main__":
    scores_df = compute_risk_score('output/wallet_features.csv')
    save_scores(scores_df, 'output/wallet_scores.csv')
    print("Risk scoring complete.")
