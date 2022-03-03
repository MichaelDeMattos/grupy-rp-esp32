# -*- coding: utf-8 -*-

from app import create_app

if __name__ == "__main__":
    create_app(host="192.168.0.135", port=5000, debug=True)
    