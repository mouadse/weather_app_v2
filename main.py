import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the secrets using os.getenv()

yandex_api_key = os.getenv("YANDEX_API_KEY")

access_key = yandex_api_key

headers = {"X-Meteum-API-Key": access_key}

query = """{
  weatherByPoint(request: { lat: 28.49462128, lon: -11.32948112 }) {
    now {
      temperature
    }
  }
}"""

response = requests.post('https://api.meteum.ai/graphql/query', headers=headers, json={'query': query})

current_weather = response.json()

weather_now = current_weather['data']['weatherByPoint']['now']['temperature']

print("The weather now is " + str(weather_now) + "°C")
