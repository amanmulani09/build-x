
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


## Core Concepts of a SDK

1. Client(entry point)
    - main class user interacts with
    - handles auth, config, and initial setup 

    eg. -> client = PaymentSDK(api_key="xyz")

2. API Layer(http handling)
    - handles requests (get,post, headers, auth etc)
    - central place for: headers, retries, error handling 

3. Resources methods (service or business logic in simple terms)
    - represet real world actions 
    - create_payment(), get_user()

4 Models 
    - structured output response
    - pydantic models 

5. Error handling 
    - convert raw api erros in clean exceptions 
    eg. raise PaymentError("Invalid API key")

6. Configuration 
    - API Key, base url, timeout and other configs 