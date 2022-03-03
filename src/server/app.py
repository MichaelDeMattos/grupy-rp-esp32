# -*- coding: utf-8 -*-

from controller import ControllerIoT
from auth_server.auth import auth_iot
from flask_restful import Api
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
api = Api(app)

def create_app(host, port, debug=True):
    api.init_app(app)
    api.add_resource(ControllerIoT, "/", "/iot_check_cmd/<string:mac>", endpoint="iot_check_cmd")
    
    return app.run(host=host, port=port, debug=debug)