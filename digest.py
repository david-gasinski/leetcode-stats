import requests
from flask import Flask, Response
from markupsafe import escape

svg_filepath = "static/digest.svg"
with open (svg_filepath, 'r') as f:
    svg_file = f.read()

app = Flask(__name__)

def populateSVG(svg: str, username: str):
    req = requests.get(f'https://leetcode-stats-api.herokuapp.com/{username}')
    req_json = req.json()
    return svg.format(easy=req_json["easySolved"], medium=req_json["mediumSolved"], hard=req_json["hardSolved"], rank=req_json["ranking"])

@app.route('/svg/<username>')
def svg(username):
    svg_text = populateSVG(svg_file, escape(username))
    return Response(svg_text, mimetype='image/svg+xml')
