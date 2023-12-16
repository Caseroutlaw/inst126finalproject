import requests
from bs4 import BeautifulSoup
import time

def get_exchange_rate():
    """
    Get real-time U.S. dollar-RMB exchange rates from Wise (https://wise.com/zh-cn/currency-converter/).
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 ...'
        }
        url = "https://wise.com/zh-cn/currency-converter/usd-to-cny-rate?amount=1"
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        rate_span = soup.find('span', class_='text-success')
        if rate_span:
            exchange_rate = rate_span.text
            return exchange_rate
        else:
            return None
    except Exception as e:
        print(f"An error occurred:{str(e)}")
        return None

# If called in a loop, it is recommended to include the following lines to avoid too frequent requests:
# sleep(10) Wait 10 seconds between requests
