from utils.load_components import svg_chart_template
from math import cos, sin, pi

def getCoordsFromDeg(angle, radius, svgSize):
    x, y = cos(angle * pi / 180), sin(angle * pi / 180)
    coordX = x * radius + svgSize / 2
    coordY = y * -radius + svgSize / 2
    return [coordX, coordY] 


def svgDonutChart(x : int , y : int, theme: object, radius: int, border_size: int, angle: int, svgSize: int):
    # due to a bug with svg coordinates, an angle of 360 produces an empty chart.
    if angle == 360:
        angle -= 0.01
    (outer_coords, inner_coords) = (
        getCoordsFromDeg(angle, radius, svgSize),
        getCoordsFromDeg(angle, radius - border_size, svgSize),
    )
    (outer_coords_full, inner_coords_full) = (
        getCoordsFromDeg(359.99, radius, svgSize),
        getCoordsFromDeg(359.99, radius - border_size, svgSize),
    )
    path_string = f"""
        M {svgSize} {radius}
        A {radius} {radius} 0 {1 if angle > 180 else 0} 0 {outer_coords[0]} {outer_coords[1]}
        L {inner_coords[0]} {inner_coords[1]}   
        A {radius- border_size} {radius-border_size} 0 {1 if angle > 180 else 0} 1 {svgSize - border_size} {radius}
    """
    full_slice = f"M {svgSize} {radius} \n A {radius} {radius} 0 1 0 {outer_coords_full[0]} {outer_coords_full[1]} \n L {inner_coords_full[0]} {inner_coords_full[1]} \n A {radius - border_size} {radius - border_size} 0 1 1 {svgSize - border_size} {radius}"
    return svg_chart_template.format(
        x=x, y=y, center_x=(x+svgSize/2), center_y=(x+svgSize/2), color=theme.green, bg_color=theme.light, path_slice=path_string, full_slice=full_slice
    )
