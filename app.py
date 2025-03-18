import logging
import json
import os
import requests
from sys import exc_info
from flask import Flask, render_template, request, redirect


# Setup up a Flask instance
app = Flask(__name__)

# Obtain time from public api
def query_dog():
    try:
        response = requests.get(
            url="https://dog.ceo/api/breeds/image/random",
            timeout=5
        )

        if response.status_code == 200:
            time = (json.loads(response.text))['message']
            return time
        elif response.status_code != 200:

            return "Unavailable"
            
    except Exception:
        return "Unavailable"


# Render the template
@app.route("/")
def index():
    todaystime = query_dog()
    return render_template('index.html', time=todaystime)
