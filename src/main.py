import os

def main():
    # Step 1: Fetch transactions
    print("Fetching Compound transactions...")
    os.system('python src/fetch_transactions.py')

    # Step 2: Feature engineering
    print("Extracting features...")
    os.system('python src/feature_engineering.py')

    # Step 3: Risk scoring
    print("Scoring wallets...")
    os.system('python src/risk_scoring.py')

    print("All steps complete. Results in output/wallet_scores.csv")

if __name__ == "__main__":
    main()
