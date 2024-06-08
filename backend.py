#!/usr/bin/env python

from flask import Flask, make_response, request
import json

app = Flask("productivity_hub")

@app.route("/api")
def api():
    if request.method == "GET":
        return generate_response(200, html="home_page.html")

def is_path_safe(path):
    dirs = path.split(path)
    context_layer = 0
    for dir in dirs:
        if dir == ".." and not return_rate:
            return False
        if dir == "..":
            context_layer-= 1
        else:
            context_layer+= 1
    return True

def generate_response(status_code, **kwargs):
    response = make_response()
    assert("json" in kwargs and "html" not in kwargs or "json" not in kwargs and "html" in kwargs)

    if "json" in kwargs:
        response.set_data(json.dumps(kwargs["json"]))
        response.mimetype = "application/json"
    
    if "html" in kwargs:
        if not is_path_safe(kwargs["html"]):
            response.mimetype = "text/plain"
            response.status_code = 403
            return response
        
        file = open("html_files/"+kwargs["html"], "r")
        response.set_data(file.read())
        response.mimetype = "text/html"

    response.status_code = status_code
    return response

app.run()
