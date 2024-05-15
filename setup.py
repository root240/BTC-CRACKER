import concurrent.futures
import time
from bitcoin import *
import requests
import colorama

# Initialize colorama
colorama.init()

# Function to generate a random private key and corresponding address
def generate_address():
    private_key = random_key()
    address = privkey_to_address(private_key)
    return private_key, address

# Function to get the balance of a Bitcoin address
def get_balance(address, token):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance?token={token}'
    response = requests.get(url)
    data = response.json()
    return data.get('final_balance', 0)

# Your API token
TOKEN = 'your_api_token_here'

def process_address():
    try:
        pr, adr = generate_address()
        balance = get_balance(adr, TOKEN)
        if balance > 0:
            with open('positive_balances.txt', 'a') as file:
                file.write(f'{pr}    {adr}    {balance}\n')
        print(colorama.Fore.BLUE + pr, '    ', colorama.Fore.GREEN + adr, 'BTC = ', balance)
    except Exception as e:
        print("An error occurred:", e)

# Open a ThreadPoolExecutor with a maximum of 10 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    while True:
        executor.submit(process_address)
        time.sleep(0.1)  # Adjust sleep time as needed

# Reset colorama settings
colorama.deinit()
