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

# grabs user data from a leetcode api and returns the svg template with the data filled in.
def populateSVG(svg: str, username: str, styling: str):
    req = requests.get(f'https://leetcode-stats-api.herokuapp.com/{username}')
    req_json = req.json()
    if (req_json['status'] == 'error'):
        return "User does not exist"
    totalProblems = int(req_json["totalEasy"]) + int(req_json["totalMedium"]) + int(req_json["totalHard"])
    totalSolved = int(req_json["easySolved"]) + int(req_json["mediumSolved"]) + int(req_json["hardSolved"])
    totalSolvedDeg = (totalSolved / totalProblems) * 360
    return svg.format(
            username=username,
            rank=req_json["ranking"],  
            easy=req_json["easySolved"], 
            medium=req_json["mediumSolved"], 
            hard=req_json["hardSolved"], 
            chart=svgDonutChart(275,30, 'lightgreen', 50, 20, totalSolvedDeg, 100),
            totalCompleted=f'{totalSolved} / {totalProblems}',
            stylesheet=styling,
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
