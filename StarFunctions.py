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
    #grab the singleton Screen
    screen = Screen()

    #get the center coordinate with pop up prompts
    pos_x = screen.numinput("X position", "center x coordinate", 0, -screen.window_width() / 2, screen.window_width() / 2)
    pos_y = screen.numinput("Y position", "center y coordinate", 0, -screen.window_height() / 2, screen.window_height() / 2)

    #get size
    diameter = screen.numinput("Diameter", "Star Diameter", 200, 1)

    #get num_points
    num_points = int(screen.numinput("Points", "Number of points", default= 5, minval= 5))
    line_width = int(screen.numinput("Line width", "Line width", default= 1, minval= 1))

    #color things
    #prompt line color
    line_color = screen.textinput("Line color", "Line color")

    #color string validation loop
    while color_invalid(line_color):
        line_color = screen.textinput("Invalid Color", "Try again")

    #default color
    if line_color == "":
        line_color = "black"

    #prompt for fill bool and make it a bool
    is_filled = screen.textinput("Fill", "Is the star colored in?")
    is_filled = is_filled.lower() == "yes" or is_filled.lower() == "true"

    if is_filled:
        #prompt for fill color
        fill_color = screen.textinput("Fill color", "Fill color")

        #color string validation loop
        while color_invalid(fill_color):
            fill_color = screen.textinput("Invalid Color", "Try again")

        #default fill color
        if fill_color == "":
            fill_color = "black"
    else:
        #insure a valid string is passed to t.color()
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
    #grab the singleton Screen
    screen = Screen()
    t = RawTurtle(screen.getcanvas())

    #set the shape of the pen
    t.shape("turtle")
    #set the line width
    t.width(star.line_width)
    #set the line and fill color
    t.color(star.line_color, star.fill_color)
    #pick up the pen
    t.penup()
    #move it to the 12 o'clock position of the star
    t.setposition(star.pos[0], star.pos[1] + star.size / 2)
    #put the pen down
    t.pendown()
    #set the initial direction of the pen
    t.setheading(270 - star.half_angle)

    return t

def color_invalid(color: str) -> bool:
    #grab the screen
    test_screen = Screen()
    #make a test turtle
    color_test = RawTurtle(test_screen.getcanvas())
    #make it invisible
    color_test.hideturtle()
    try:
        #try to set the color to 'color' and delete the turtle
        color_test.pencolor(color)
        test_screen.clearscreen()
        return False
    except TurtleGraphicsError:
        #if an exception is thrown:
        test_screen.clearscreen()
        return True