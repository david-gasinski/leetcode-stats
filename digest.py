from flask import Flask, Response, request, render_template
from markupsafe import escape
from lib.chart import svgDonutChart
from utils.load_components import svg_template
from utils.load_components import default_theme
from lib.style import fetchCustomCSS
from lib.user import User
from lib.themes import Theme

app = Flask(__name__)


# grabs user data from a leetcode api and returns the svg template with the data filled in.
def populateSVG(svg: str, username: str, styling: str, theme: dict):
    data = User(username)
    return svg.format(
            username=data.username,
            rank=data.ranking,  
            easy=data.easySolved, 
            medium=data.mediumSolved, 
            hard=data.hardSolved, 
            chart=svgDonutChart(275,30, theme.green, theme.light, 50, 20, data.solvedDeg, 100),
            totalCompleted=f'{data.totalSolved} / {data.totalQuestions}',
            stylesheet=styling,
            theme = theme
        )

# returns the generated svg with a given user name
@app.route('/svg/<username>')
def svg(username):
    custom_stylesheet = request.args.get('stylesheet')
    custom_theme = request.args.get('theme')

    if custom_theme == None:
        # default theme is nord
        custom_theme = 'nord'
    
    if custom_stylesheet == None:
        custom_stylesheet = default_theme
    else:
        custom_stylesheet = fetchCustomCSS(custom_stylesheet)

    theme = Theme(custom_theme)
        
    svg_text = populateSVG(svg_template, escape(username), custom_stylesheet, theme)
    return Response(svg_text, mimetype='image/svg+xml')

# app to customise svg
@app.route('/')
def customiseSVG():
    return render_template('index.html')

    