# -*- coding: utf-8 -*-

import traceback
from model import db
from flask_restful import Resource
from auth_server.auth import auth_iot
from flask import make_response, jsonify

class ControllerIoT(Resource):
    def __init__(self, *agrs):
        pass
    
    @auth_iot
    def get(self, mac):
        try:
            return make_response(jsonify({"status": "200", "mac": mac}, 200))
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"status": "403", "error": error}, 403))