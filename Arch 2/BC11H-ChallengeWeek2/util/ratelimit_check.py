from dotenv import load_dotenv
import requests
import time
import os

load_dotenv()

url = 'https://api.codehunt.nl/categories/clnx6wdxc0004od0uemi4n473/exercises/clnx7862s000cod0ukp5u511h'

# Make initial request to get ratelimit info
auth_header = os.getenv("AUTH_KEY")
headers = {"Authorization": auth_header}
cookies = {
    "cf_clearance": "cf_clearance=pItVeAQKg0c09UJOM35TxD2pCMujyteolRgnJxrZXew-1698827256-0-1-6a5ff80b.8cb6497b.e13d4d43-160.0.0; Path=/; Domain=codehunt.nl; Secure; HttpOnly;"
}

response = requests.post(url=url, headers=headers, cookies=cookies)
ratelimit_remaining = response.headers.get('X-RateLimit-Remaining')
ratelimit_reset = response.headers.get('X-RateLimit-Reset')

if ratelimit_remaining is not None:
    print(f'Rate limit remaining: {ratelimit_remaining}')
if ratelimit_reset is not None:
    print(f'Rate limit resets at: {ratelimit_reset}')

# Keep making requests while tracking ratelimit
count = 0
max_count = 10
while count != max_count:
    response = requests.get(url)
    ratelimit_remaining = response.headers.get('X-RateLimit-Remaining')

    if ratelimit_remaining == 0:
        print('[1] Rate limit exceeded, sleeping until reset...')
        time.sleep(int(ratelimit_reset) - time.time())
        count += 1

        continue
    if response.status_code == 429:
        print('[2] Rate limit exceeded, sleeping until reset...')
        time.sleep(6)
        count += 1
        continue

    if 'cloudflare' in response.text.lower():
        print("Cloudflare intervened....trying again..")
        print(response.text.lower())
        time.sleep(6)
        count += 1
        continue

    print('Fetched data successfully!')
    count += 1
print("Done")
