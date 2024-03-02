# import random
# import time
#
# symbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
#
#
# while True:
#     stringus = "https://discord.gg/"
#     code = ""
#     for i in range(8):
#         a = random.choice(symbols)
#         code = code + a
#
#     print(stringus+code)
#     time.sleep(3)


import requests
import datetime

# Replace 'YOUR_API_KEY' with your actual API key from Alpha Vantage
API_KEY = 'YOUR_API_KEY'

# Function to get historical currency exchange rates
def get_currency_exchange_rates(base_currency, target_currency, api_key):
    # Calculate dates for one month period
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')

    # Construct the API request URL
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={base_currency}&to_symbol={target_currency}&apikey={api_key}&outputsize=full&datatype=json'

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Extract exchange rates from the response
    exchange_rates = {}
    for date, info in data['Time Series FX (Daily)'].items():
        if date >= start_date and date <= end_date:
            exchange_rates[date] = float(info['4. close'])

    return exchange_rates

# Example usage
base_currency = 'USD'  # Base currency
target_currency = 'EUR'  # Target currency
exchange_rates = get_currency_exchange_rates(base_currency, target_currency, API_KEY)

# Print exchange rates
for date, rate in exchange_rates.items():
    print(f'{date}: {rate}')
