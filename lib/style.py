import requests
from utils.load_components import default_theme

def fetchCustomCSS(url: str):
    """
    Fetches external stylesheet. If length is above 1000 characters returns default theme
    """
    css = requests.get(url).text
    if len(css) > 1000:
        return default_theme
    else:
        return css
