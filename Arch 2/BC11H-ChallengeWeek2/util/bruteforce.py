import os
import requests
from dotenv import load_dotenv
from time import sleep

load_dotenv()


def send_request(item, url):
    data = {"answer": str(item)}
    auth_header = os.getenv("AUTH_KEY")
    headers = {"Authorization": auth_header}
    cookies = {
        "cf_clearance": "cf_clearance=pItVeAQKg0c09UJOM35TxD2pCMujyteolRgnJxrZXew-1698827256-0-1-6a5ff80b.8cb6497b.e13d4d43-160.0.0; Path=/; Domain=codehunt.nl; Secure; HttpOnly;"
    }

    try:
        response = requests.post(url, data, headers=headers, cookies=cookies)
        if 200 <= response.status_code < 300:
            return response
    except KeyboardInterrupt:
        raise
    except BaseException as ex:
        print("Caught Exception: ", ex.args)
    print(f"retrying {item}...")
    sleep(500)  # wait at least half a second before retrying
    return send_request(item, url)


def send_items(items, url):
    print(f"Bruteforcing {len(items)} items...")
    for item in items:
        print(item)
        if send_request(item, url).json(["completed"]):
            return item
