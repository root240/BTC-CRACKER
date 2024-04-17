from bitcoin import *
import requests

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
    # Infinite loop - you might want to add a condition to stop the loop
    while True:
        pr, adr = generate_address()
        balance = get_balance(adr, TOKEN)
        
        # Check if the balance is greater than 0
        if balance > 0:
            # Write the private key, address, and balance to the file
            file.write(f'{pr}    {adr}    {balance}\n')

        # Print the private key, address, and balance
        print(pr, '    ', adr, balance)
