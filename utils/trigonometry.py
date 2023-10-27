from math import cos, sin, pi

def getCoordsFromDeg(angle, radius, svgSize):
    x, y = cos(angle * pi / 180), sin(angle * pi / 180)
    coordX = x * radius + svgSize / 2
    coordY = y * -radius + svgSize / 2
    return [coordX, coordY] 
