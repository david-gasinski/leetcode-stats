from flask import Flask, Response, request, render_template
from markupsafe import escape
from lib.chart import svgDonutChart
from utils.load_components import svg_template
from utils.load_components import default_theme
from lib.style import fetchCustomCSS
from lib.user import User

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
    data = User(username)
    return svg.format(
            username=data.username,
            rank=data.ranking,  
            easy=data.easySolved, 
            medium=data.mediumSolved, 
            hard=data.hardSolved, 
            chart=svgDonutChart(275,30, 'lightgreen', 50, 20, data.solvedDeg, 100),
            totalCompleted=f'{data.totalSolved} / {data.totalQuestions}',
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

@app.route('/')
def customiseSVG():
    return render_template('index.html')

    