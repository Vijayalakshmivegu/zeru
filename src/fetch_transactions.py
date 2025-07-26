import requests
import pandas as pd
import time

# Set your Etherscan API key here
ETHERSCAN_API_KEY = 'S9TFQ3JK26HWNI8676FX34VE8XAK8PI61I'

COMPOUND_V2_ADDRESS = '0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b'
COMPOUND_V3_ADDRESS = '0xc3d688b66703497daa19211eedff47f25384cdc3'  # Example, update as needed

def fetch_wallet_transactions(wallet_address, contract_address, start_block=0, end_block=99999999):
    """
    Fetches all transactions for a wallet interacting with a given contract (Compound V2/V3) using Etherscan API.
    """
    url = (
        f'https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}'
        f'&contractaddress={contract_address}&startblock={start_block}&endblock={end_block}&sort=asc&apikey={ETHERSCAN_API_KEY}'
    )
    response = requests.get(url)
    print(response.json())
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1':
            return data['result']
        else:
            return []
    else:
        return []

def fetch_all_wallets(wallet_list, contract_address, delay=0.2):
    """
    Fetch transactions for all wallets in the list for a given Compound contract.
    """
    all_data = {}
    for wallet in wallet_list:
        print(f"Fetching transactions for {wallet}...")
        txs = fetch_wallet_transactions(wallet, contract_address)
        all_data[wallet] = txs
        time.sleep(delay)  # To avoid rate limits
    return all_data

def save_transactions_to_csv(all_data, output_path):
    """
    Save all transactions to a CSV file (one row per transaction).
    """
    rows = []
    for wallet, txs in all_data.items():
        for tx in txs:
            tx['wallet'] = wallet
            rows.append(tx)
    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Example usage: load wallets from data/wallets.csv
    wallets_df = pd.read_csv('data/wallets.csv')
    wallet_list = wallets_df.iloc[:,0].tolist()
    # Fetch Compound V2 transactions
    all_data = fetch_all_wallets(wallet_list, COMPOUND_V2_ADDRESS)
    save_transactions_to_csv(all_data, 'output/compound_v2_transactions.csv')
    print("Done fetching and saving transactions.")
