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

# Open a file in append mode
with open('positive_balances.txt', 'a') as file:
    while True:
        try:
            pr, adr = generate_address()
            balance = get_balance(adr, TOKEN)
            if balance > 0:
                file.write(f'{pr}    {adr}    {balance}\n')
            print(colorama.Fore.BLUE + pr, '    ', colorama.Fore.GREEN + adr, 'BTC = ', balance)
        except Exception as e:
            print("An error occurred:", e)
            time.sleep(5)  # Wait for 5 seconds before retrying

# Reset colorama settings
colorama.deinit()
