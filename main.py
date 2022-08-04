# -*- coding: utf-8 -*-

import time
import ujson
from machine import Pin
import urequests as requests
from boot import wlan, connect_wifi

device_id = 1
gpio_pin = Pin(2, Pin.OUT)
user = "iot@dotpyc.com"
password = "iot@123"
host = "https://dotpyc.com"
api_manager_iot = "/api/admin/manager/iot"
api_login = "/api/login"


def login(host, api, user, password):
    try:
        data_post = ujson.dumps({"email": user, "secret": password})
        req = requests.post(
            url=host + api, headers={'content-type': 'application/json'}, data=data_post)
        if req.status_code != 200:
            return ""
        return req.json().get("response")
    except Exception as error:
        print(error)
        return ""


def handler_iot(host, api, token, params):
    try:
        req = requests.get(url=host + api + params,
                           headers={"content-type": "application/json", "Authorization": token})
        if req.status_code != 200:
            return ""
        resp = req.json().get("response")
        if resp:
            gpio_pin.value(1)
            return resp
        else:
            gpio_pin.value(0)
            return resp
    except Exception as error:
        print(error)
        return ""


if __name__ == "__main__":
    try:
        if wlan.isconnected():
            token = login(host, api_login, user, password)
        else:
            connect_wifi()
            token = login(host, api_login, user, password)

        while True:
            if token and wlan.isconnected:
                handler_iot(host, api_manager_iot, token, "?device_id=1")
            else:
                if wlan.isconnected():
                    token = login(host, api_login, user, password)
                else:
                    connect_wifi()
                    token = login(host, api_login, user, password)
            time.sleep(10)
    except Exception as error:
        print(error)
