
SDK(software development kit) - An SDK is just a wrapper around an API/service that makes it easy for developers to use.

👉 instead of using this :::

import requests

response = requests.post(
    "https://api.payment.com/create",
    json={"amount": 100}
)

👉 Developers use your SDK like this:

client = PaymentSDK(api_key="xyz")
client.create_payment(amount=100)

💡 SDK = Clean interface + abstraction + developer experience