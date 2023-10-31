import requests
from flask import Flask, Response, request
from markupsafe import escape
from lib.chart import svgDonutChart
from utils.load_components import svg_template
from utils.load_components import default_theme
from lib.style import fetchCustomCSS

app = Flask(__name__)

nord_colours = {
    'dark ': '#2e3440',
    'light' : '#eceff4',
    'green' : '#a3be8c',
    'yellow' : '#ebcb8b',
    'red' : '#bf616a',
}

def populateSVG(svg: str, username: str, styling: str):
    req = requests.get(f'https://leetcode-stats-api.herokuapp.com/{username}')
    req_json = req.json()
    totalProblems = int(req_json["totalEasy"]) + int(req_json["totalMedium"]) + int(req_json["totalHard"])
    totalSolved = int(req_json["easySolved"]) + int(req_json["mediumSolved"]) + int(req_json["hardSolved"])
    totalSolvedDeg = (totalSolved / totalProblems) * 360
    return svg.format(
            easy=req_json["easySolved"], 
            medium=req_json["mediumSolved"], 
            hard=req_json["hardSolved"], 
            rank=req_json["ranking"],  
            totalSolved=totalSolved,
            totalProblems=totalProblems,
            chart=svgDonutChart(40,135, 'lightgreen', 25, 5, totalSolvedDeg, 50),
            stylesheet=styling
        )

@app.route('/svg/<username>')
def svg(username):
    custom_stylesheet = request.args.get('stylesheet')
    if custom_stylesheet == None:
        custom_stylesheet = default_theme
    else:
        custom_stylesheet = fetchCustomCSS(custom_stylesheet)
    svg_text = populateSVG(svg_template, escape(username), custom_stylesheet)
    return Response(svg_text, mimetype='image/svg+xml')
