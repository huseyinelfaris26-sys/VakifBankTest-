from vakifBank import VakifClient

client = VakifClient(api_key="YOUR_KEY")
balance = client.get_balance(account_id=12345)
print(balance)
