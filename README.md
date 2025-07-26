# Wallet Risk Scoring

This project fetches on-chain transaction data for a list of wallet addresses (from Compound V2/V3), engineers risk-related features, and assigns a risk score (0-1000) to each wallet.

## Structure
- `src/` - Source code for data fetching, feature engineering, and scoring
- `data/` - Input data (wallet list)
- `output/` - Output CSV with wallet scores

## How to Use
1. Place the wallet list in `data/wallets.csv` (one address per line or as provided).
2. Run the main script to fetch data, process features, and generate scores.
3. Results will be saved in `output/wallet_scores.csv`.

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Deliverables
- `output/wallet_scores.csv` with columns: `wallet_id`, `score`
- Brief methodology in this README

## Methodology (to be completed after implementation)
- Data Collection method
- Feature selection rationale
- Scoring method
- Justification of risk indicators
