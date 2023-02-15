from requests import get
import requests

params = {
    'q': 'MmJhODcyNjA1YWQ3NDY2ZWFmOTdhMmJmOTYyNDYxMzAuZEtoVEJJbDhSTDF0clFmWDVWWDJvN2RhQ3oxdGxyRHA1YjJoUU1wdExDSzVhU3ZMdzZZNHFaRTQ2bzBvUVdoREJpNEtPc242NHlmOVBWSlVyNlhBbGc',
}

ip = get('https://api.ipify.org').text

ip_log = open("ipublic.txt","r").readline(30)

if ip == ip_log:
    print("la ip no ha cambiado")
else:
    response = requests.get('https://ipv4.api.hosting.ionos.com/dns/v1/dyndns', params=params)
    open("ipublic.txt","w").write(str(ip))
    print("la ip ha cambiado")

