import requests
from flask import Flask, Response
from markupsafe import escape
from lib.chart import svgDonutChart
from utils.load_components import svg_template

app = Flask(__name__)

def populateSVG(svg: str, username: str):
    req = requests.get(f'https://leetcode-stats-api.herokuapp.com/{username}')
    req_json = req.json()
    return svg.format(
            easy=req_json["easySolved"], 
            medium=req_json["mediumSolved"], 
            hard=req_json["hardSolved"], 
            rank=req_json["ranking"],  
            chart=svgDonutChart('lightgreen',40, 20, 270, 80)
        )

@app.route('/svg/<username>')
def svg(username):
    svg_text = populateSVG(svg_template, escape(username))
    return Response(svg_text, mimetype='image/svg+xml')
