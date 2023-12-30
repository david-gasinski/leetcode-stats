from flask import Flask, Response, request, render_template
from markupsafe import escape
from utils.load_components import svg_template
from lib.user import User
from lib.themes import Theme

app = Flask(__name__)


# grabs user data from a leetcode api and returns the svg template with the data filled in.
def populateSVG(svg: str, username: str, theme: dict):
    user = User(username, theme)
    user.fetchData()
    return user.svg


# returns the generated svg with a given user name
@app.route('/svg/<username>')
def svg(username):
    custom_theme = request.args.get('theme')

    if custom_theme == None:
        # default theme is nord
        custom_theme = 'nord'

    theme = Theme(custom_theme)
        
    svg_text = populateSVG(svg_template, escape(username), theme)
    return Response(svg_text, mimetype='image/svg+xml')

# app to customise svg
@app.route('/')
def customiseSVG():
    return render_template('index.html')

    