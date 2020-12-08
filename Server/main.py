import json
from flask import Flask, request, current_app, g, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

api.add_resource(DAO, '/DAO/<command>')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == '__main__':
    app.run(port='5002')
