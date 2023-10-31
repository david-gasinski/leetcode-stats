with open ('static/digest.svg', 'r') as f:
    svg_template = f.read()
with open ('static/components/chart.svg', 'r') as c:
    svg_chart_template = c.read()
with open('static/css/default_theme.css', 'r') as f:
    default_theme = f.read()