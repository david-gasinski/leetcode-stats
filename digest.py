from flask import Flask, Response, request, render_template
from markupsafe import escape
from lib.chart import svgDonutChart
from utils.load_components import svg_template
from utils.load_components import default_theme
from lib.user import User
from lib.themes import Theme

app = Flask(__name__)


# grabs user data from a leetcode api and returns the svg template with the data filled in.
def populateSVG(svg: str, username: str, animation: str,  theme: dict):
    data = User(username)

    with open('./static/animation.svg', 'r') as f: animation = f.read()
    with open('./static/font.svg', 'r') as g: font = g.read()

    return svg.format(
            username=data.username,
            rank=data.ranking,  
            easy=data.easySolved, 
            medium=data.mediumSolved, 
            hard=data.hardSolved, 
            chart=svgDonutChart(275,30, theme, 50, 20, data.solvedDeg, 100),
            totalCompleted=f'{data.totalSolved} / {data.totalQuestions}',
            theme = theme,
            animation = animation,
            font = font
        )

# returns the generated svg with a given user name
@app.route('/svg/<username>')
def svg(username):
    custom_theme = request.args.get('theme')

    if custom_theme == None:
        # default theme is nord
        custom_theme = 'nord'

    theme = Theme(custom_theme)

    with open('./static/animation.svg', 'r') as f:
        animation = f.read()
        
    svg_text = populateSVG(svg_template, escape(username), animation, theme)
    return Response(svg_text, mimetype='image/svg+xml')

# app to customise svg
@app.route('/')
def customiseSVG():
    return render_template('index.html')

    