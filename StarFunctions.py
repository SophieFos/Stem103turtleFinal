import math
from dataclasses import dataclass
from turtle import RawTurtle, Screen, TurtleGraphicsError


@dataclass
class StarData:
    pos: tuple[float, float]
    size: float
    num_points: int
    line_color: str
    line_width: int
    is_filled: bool
    fill_color: str
    chord_angle: float
    half_angle: float


def get_input() -> StarData:
    screen = Screen()

    #get the center coordinate
    pos_x = screen.numinput("X position", "center x coordinate", 0, -screen.window_width() / 2, screen.window_width() / 2)
    pos_y = screen.numinput("Y position", "center y coordinate", 0, -screen.window_height() / 2, screen.window_height() / 2)

    #get size
    diameter = screen.numinput("Diameter", "Star Diameter", 200, 1)

    #get num_points
    num_points = int(screen.numinput("Points", "Number of points", default= 5, minval= 5))
    line_width = int(screen.numinput("Line width", "Line width", default= 1, minval= 1))

    #color things

    line_color = screen.textinput("Line color", "Line color")
    while not color_valid(line_color):
        line_color = screen.textinput("Invalid Color", "Try again")
    if line_color == "":
        line_color = "black"

    is_filled = screen.textinput("Fill", "Is the star colored in?")
    is_filled = is_filled.lower() == "yes" or is_filled.lower() == "true"

    if is_filled:
        fill_color = screen.textinput("Fill color", "Fill color")
        while not color_valid(fill_color):
            fill_color = screen.textinput("Invalid Color", "Try again")
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

def init_turtle(star: StarData) -> RawTurtle:

    screen = Screen()
    t = RawTurtle(screen.getcanvas())

    t.shape("turtle")
    t.width(star.line_width)
    t.color(star.line_color, star.fill_color)
    t.penup()
    t.setposition(star.pos[0], star.pos[1] + star.size / 2)
    t.pendown()
    t.setheading(270 - star.half_angle)

    return t

def color_valid(color: str) -> bool:
    is_valid = True

    test_screen = Screen()
    color_test = RawTurtle(test_screen.getcanvas())
    color_test.hideturtle()
    try:
        color_test.pencolor(color)
        test_screen.clearscreen()
        return is_valid
    except TurtleGraphicsError:
        is_valid = False
        test_screen.clearscreen()
        return is_valid