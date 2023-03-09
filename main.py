import asyncio
import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()


async def fetch_weather():
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
    async with aiohttp.ClientSession() as session:
        async with session.post('https://api.meteum.ai/graphql/query', headers=headers,
                                json={'query': query}) as response:
            current_weather = await response.json()
            weather_now = current_weather['data']['weatherByPoint']['now']['temperature']
            print(f"The weather now is {weather_now}°C")


async def main():
    await fetch_weather()


if __name__ == '__main__':
    asyncio.run(main())
