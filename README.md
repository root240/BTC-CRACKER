### BTC CRACKER

Here is a more detailed breakdown of the script's steps:

Generate a private key: The script uses a cryptographically secure random number generator to generate a 256-bit hexadecimal private key. This private key is essential for accessing the corresponding Bitcoin wallet.

Convert private key to public key: The generated private key is then used to derive the corresponding public key. The public key is used to receive Bitcoin transactions and is shared with others to allow them to send Bitcoin to the wallet.

Check wallet balance: The script uses the public key and the wallet's API to query the blockchain and retrieve the current balance of the wallet. The API response contains the balance in Bitcoin units.

Print results: The script prints the following information to the console:

Private key: The hexadecimal representation of the generated private key
Public key: The hexadecimal representation of the derived public key
Balance: The current balance of the wallet in Bitcoin units
Save positive balances: If the wallet balance is greater than zero, the script writes the following information to a file called positive_balances.txt;


### Requirements

 Python 3 or higher is required
 `pip install bitcoin`
`pip install requests`
`pip install colorama`

### HOW TO USE

for linux users
`python3 setup.py`

for windows users
`python setup.py`
