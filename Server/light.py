import json
from flask import Response
from flask_restful import request, Resource


class Light(Resource):
    def post(self, command):
        if command == 'set':
