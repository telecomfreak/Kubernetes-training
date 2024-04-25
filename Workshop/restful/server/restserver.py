#!/usr/bin/env python3

import json
import flask

PORT = 8080

app = flask.Flask(__name__)

# prepare response to be returned to client
#
def prep_response(obj):
    body = json.dumps(obj)
    resp = flask.make_response(body)
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Content-Length'] = len(body)
    return resp


# handle /products 
#
@app.route("/products")
def products():
    return prep_response([42])


# handle /products/42: read product description from file
#
@app.route("/products/42")
def products42():
    try:
        with open('descriptions/bananas') as f: desc = f.read()
    except Exception:
        desc = "Unknown"

    return prep_response({'id':'42', 'name': 'Bananas', 'description': desc})


app.run(host="0.0.0.0", port=PORT)
