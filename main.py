import requests
import time

# File containing token lines (one per account)
TOKENS_FILE = "tokens.txt"
URL = "https://faucetearner.org/api.php?act=faucet"

# Common headers for the request
HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://faucetearner.org',
    'referer': 'https://faucetearner.org/faucet.php',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

def send_claim_request(pid):
    """Send a faucet claim request for a specific PID."""
    cookie = f"pid={pid}; googtrans=/en/en; reg=1; login=1; user={pid}-197.166.101.13; show_nt1=1;"
    HEADERS['cookie'] = cookie
    try:
        response = requests.post(URL, headers=HEADERS, json={})
        if response.status_code == 200:
            print(f"Success for PID {pid}: {response.json()}")
        else:
            print(f"Error for PID {pid}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed for PID {pid}: {e}")

def main():
    # Read all PIDs from tokens file
    with open(TOKENS_FILE, 'r') as file:
        pids = [line.strip() for line in file if line.strip()]

    while True:
        start_time = time.time()

        for pid in pids:
            send_claim_request(pid)

        # Calculate elapsed time and adjust delay to ensure 60-second intervals
        elapsed_time = time.time() - start_time
        sleep_time = max(0, 60 - elapsed_time)
        print(f"Sleeping for {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
