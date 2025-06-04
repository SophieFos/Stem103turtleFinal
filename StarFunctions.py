import math
from dataclasses import dataclass
from turtle import RawTurtle, Screen

@dataclass
class StarData:
    pos: tuple[int, int]
    size: float
    num_points: int
    line_color: str
    line_width: int
    is_filled: bool
    fill_color: str
    chord_angle: float
    half_angle: float


def get_input(screen: Screen) -> StarData:
    #get the center coordinate
    pos_x = screen.numinput("X position", "center x coordinate", 0, -screen.window_width() / 2, screen.window_width() / 2)
    pos_y = screen.numinput("Y position", "center y coordinate", 0, -screen.window_height() / 2, screen.window_height() / 2)

    #get size
    diameter = screen.numinput("Diameter", "Star Diameter", 200, 1)

    #get num_points
    num_points = int(screen.numinput("Points", "Number of points", default= 5, minval= 5))

    #color things
    line_width = int(screen.numinput("Line width", "Line width", default= 1, minval= 1))
    line_color = screen.textinput("Line color", "Line color")
    if line_color == "":
        line_color = "black"
    is_filled = screen.textinput("Fill", "Is the star colored in?")
    is_filled = is_filled.lower() == "yes" or is_filled.lower() == "true"

    if is_filled:
        fill_color = screen.textinput("Fill color", "Fill color")
        if fill_color == "":
            fill_color = "black"
    else:
        fill_color = "black"

    # calculate chord angle and half angle
    if num_points % 2:
        chord_angle = (math.tau / num_points) * (num_points // 2)
        half_angle = (180 - math.degrees(chord_angle)) / 2
    else:
        second_point_index = int(num_points * .5 - 1)

        #make sure the second point is coprime to the number of points
        while math.gcd(second_point_index, num_points) != 1:
            second_point_index -= 1
        chord_angle = (math.tau / num_points) * second_point_index
        half_angle = (180 - math.degrees(chord_angle)) / 2

    star = StarData((pos_x, pos_y), diameter, num_points, line_color, line_width, is_filled, fill_color, chord_angle, half_angle)
    return star

def init_turtle(screen: Screen, star: StarData) -> RawTurtle:

    t = RawTurtle(screen.getcanvas())

    t.shape("turtle")
    t.width(star.line_width)
    set_colors(t, star)
    t.penup()
    t.setposition(star.pos[0], star.pos[1] + star.size / 2)
    t.pendown()
    t.setheading(270 - star.half_angle)

    return t

def set_colors(turtle: RawTurtle, star: StarData) -> None:

    #set the line color
    try:
        turtle.pencolor(star.line_color)
    except:
        turtle.pencolor("black")

    #set the fill color
    try:
        turtle.fillcolor(star.fill_color)
    except:
        turtle.fillcolor("black")