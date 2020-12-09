import json
import time
import random
import constant
from flask import Response
from flask_restful import request, Resource
from miio import Yeelight


class Light(Resource):
    def get(self, command):
        bulb = Yeelight(constant.IP, constant.TOKEN)
        if command == 'toggle':
            if bulb.status().is_on:
                bulb.off()
                return Response(response='Turn off', status=200)
            else:
                bulb.on()
                return Response(response='Turn on', status=200)
        elif command == 'set':
            r = int(request.args.get('r'))
            g = int(request.args.get('g'))
            b = int(request.args.get('b'))
            bulb.on()
            bulb.set_rgb([r, g, b])
            return Response(response='Turn on with (' + str(r) + ', ' + str(g) + ', ' + str(b) + ')', status=200)
        elif command == 'bright':
            bright = int(request.args.get('bright'))
            bright = 100 if bright > 100 else bright
            if bright > 0:
                bulb.on()
                bulb.set_brightness(bright)
                resp = Resp('Brightness set to ' + str(bright), 'on')
                return Response(response=json.dumps(resp.getJSON()), status=200, mimetype="application/json")
            else:
                bulb.off()
                resp = Resp('Light is turn off', 'off')
                return Response(response=json.dumps(resp.getJSON()), status=200, mimetype="application/json")
        elif command == 'random':
            random.seed(time.time())
            r = random.randrange(0, 255)
            g = random.randrange(0, 255)
            b = random.randrange(0, 255)
            bulb.on()
            bulb.set_rgb([r, g, b])
            resp = Resp('Turn on with (' + str(r) + ', ' +
                        str(g) + ', ' + str(b) + ')', [r, g, b])
            return Response(response=json.dumps(resp.getJSON()), status=200, mimetype='application/json')
        elif command == 'status':
            resp = Resp("status", bulb.status().__dict__)
            return Response(response=json.dumps(resp.getJSON()), status=200, mimetype='application/json')


class Resp:
    def __init__(self, message, ret):
        self.message = message
        self.ret = ret

    def getJSON(self):
        return {
            "message": self.message,
            "return": self.ret
        }
