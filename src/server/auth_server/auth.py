# -*- coding: utf-8 -*-

import binascii
import traceback
from model import db
from functools import wraps
from flask import request, make_response, jsonify

""" Simple Auth To IoT """
def auth_iot(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            auth = request.headers["Authorization"].replace("Basic ", "").replace("b'", "").replace("'", "")
            token = binascii.a2b_base64(f"{auth}".encode())
            
        except Exception as error:
            traceback.print_exc()
            return make_response(jsonify({"status": 403, "error": error}, 403))
        
        
        return f(*args, **kwargs)
    
    return decorated

