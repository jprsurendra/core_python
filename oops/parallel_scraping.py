import threading
import requests
import time
from datetime import datetime

# URL = "http://localhost:8001/api/searchquotes/quote-search-result/39763/?data_source=LINER_SPOT&spot_carrier=MSCU&get_spot_rate=True"

quote_id = 39742
carrier_codes = ["MSCU", "ONEY", "HLCU", "MSCU", "ONEY", "CMDU", "MAEU"]

TOKEN = "2KrmoCbJLyDcdgaJZYaiQNyeWCYtPacu"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Cookie": 'fcsrftoken={TOKEN}; sessionid=n82sms53pt66vdjjkf8x7mac2qhpaimk'
}
HEADERS["X-CSRFToken"] = f"{TOKEN}"


NUM_THREADS = len(carrier_codes)   # ✅ fix
barrier = threading.Barrier(NUM_THREADS)


def fetch_data(quote_id, carrier_code):
    thread_name = f"Thread-{quote_id}-{carrier_code}"
    _url = f"http://localhost:8001/api/searchquotes/quote-search-result/{quote_id}/?data_source=LINER_SPOT&spot_carrier={carrier_code}&get_spot_rate=True"

    barrier.wait()

    start = time.time()
    start_dt = datetime.now()

    try:
        print(f"{thread_name} START at {start_dt.strftime('%H:%M:%S.%f')}")
        print(f"{thread_name} URL: {_url}")

        response = requests.get(_url, headers=HEADERS, timeout=30)

        end = time.time()
        end_dt = datetime.now()
        duration = round(end - start, 3)

        print(f"{thread_name} END   at {end_dt.strftime('%H:%M:%S.%f')}")
        print(f"{thread_name} TOOK  {duration} sec | status={response.status_code}")

        # print limited response (avoid huge logs)
        print(f"{thread_name} RESPONSE (first 200 chars): {response.text[:200]}")

    except Exception as e:
        end = time.time()
        print(f"{thread_name} ERROR after {round(end - start, 3)} sec:", e)


threads = []

total_start = time.time()

for carrier_code in carrier_codes:
    t = threading.Thread(target=fetch_data, args=(quote_id, carrier_code))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

total_end = time.time()

print("\nTOTAL TIME:", round(total_end - total_start, 3), "sec")