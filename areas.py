import math

def area_triangle(base, height):
    return 0.5 * base * height

def area_rect(width, height):
    return width * height

def surf_area_cuboid(width, height, depth):
    return 2*(width * height) + 2*(height * depth) + 2*(depth*width)

def area_circ(radius):
    return math.pi * radius**2

def area_trapezium(base, top, height):
    return 0.5 * height * (base + top)

