import requests

# fetches external stylesheet and embeds it in the svg
def fetchCustomCSS(url: str):
    css = requests.get(url).text
    if len(css) > 1000:
        return
    else:
        return css
