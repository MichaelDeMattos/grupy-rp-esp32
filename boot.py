# -*- coding: utf-8 -*-

import time
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)


def connect_wifi():
    while not wlan.isconnected():
        try:
            wlan.connect("Michael2.4G", "Michael2.4G")
            time.sleep(1)
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    connect_wifi()
