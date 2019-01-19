from flask import Flask, render_template, request
import json
import requests
import time
import tasks
import random



app1 = Flask(__name__)


@app1.route('/saurabh', methods=['POST'])
def index():
    x = request.json
    # print(x)
    #print(x["userId"])
    # at = random.choice()
    tasks.perform.delay(x['userId'], x['videoId'])
    return "Flask working"

if __name__ == "__main__":
    app1.run(debug=True)