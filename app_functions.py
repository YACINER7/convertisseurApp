import requests


def get_rates(api_key, base="EUR"):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    response = requests.get(url)
    data = response.json()
    if data["result"] != "success":
        return None
    return data["conversion_rates"]


def convert(amount, from_currency, to_currency, rates):
    if amount <= 0:
        return None
    if from_currency == to_currency:
        return amount
    return amount * rates[to_currency] / rates[from_currency]
