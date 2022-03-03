# -*- coding: utf-8 -*-

import time
import json
import socket
import ubinascii
from machine import Pin
from boot import connect_wifi, wlan

GPIO_RELAY = Pin(22, Pin.OUT)
MAC = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
MODEL = "PYC-01"
SERIE = "001"
TOKEN = str(ubinascii.b2a_base64(f"{MAC}|{MODEL}|{SERIE}"))
SERVER = f"http://192.168.0.135/iot_check_cmd/{MAC}"


""" REQUEST HTTP USING SOCKET """
def http_get(url):
    response = ""
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 5000)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes(
        "GET /%s HTTP/1.0\r\nHost: %s\r\n"
        "Authorization: Basic %s\r\n\r\n" % (path, host, TOKEN), 'utf8'))
    while True:
        data = s.recv(1024)
        if data:
            response = data
        else:
            break

    s.close()
    response = str(response).replace("b'", "'")
    response = response.split("GMT")
    if len(response) > 1:
        response = json.loads(
            response[1].replace("\\r", "").replace("\\n", "").replace("'", ""))
        return response
    else:
        return {"status": 403}

if __name__ == "__main__":
    while True:
        try:

            if wlan.isconnected():
                req = http_get(url=SERVER)
            
            else:
                connect_wifi()

            time.sleep(10)

        except Exception as error:
            print(error)
            time.sleep(5)
