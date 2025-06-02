from dataclasses import dataclass
from turtle import RawTurtle, Screen

@dataclass
class StarData:
    pos: tuple[int, int] = (0,0)
    size: float = 200
    num_points: int = 5
    line_color: str = "black"
    is_filled: bool = False
    fill_color: str = "black"
    half_angle: float = 18


def get_input(screen: Screen) -> StarData:
    #get the center coordinate
    pos_x = screen.numinput("X position", "center x coordinate", 0, -screen.window_width() / 2, screen.window_width() / 2)
    pos_y = screen.numinput("Y position", "center y coordinate", 0, -screen.window_height() / 2, screen.window_height() / 2)

    #get size
    diameter = screen.numinput("Diameter", "Star Diameter", 200, 1, min(screen.window_width(), screen.window_height()))

    #get num_points
    points = int(screen.numinput("Points", "Number of points", 5, 5))

    #color things
    line_color = screen.textinput("Line color", "Line color")
    is_filled = screen.textinput("Fill", "Is the star colored in?")
    is_filled = is_filled.lower() == "yes" or is_filled.lower() == "true"

    if is_filled:
        fill_color = screen.textinput("Fill color", "Fill color")
    else:
        fill_color = "black"

    #odd pointed star
    if points % 2:
        half_angle = 360 / points / 4
    #even pointed star
    else:
        half_angle = 360 / points / 2

    star = StarData((pos_x, pos_y), diameter, points, line_color, is_filled, fill_color, half_angle)
    return star

def init_turtle(screen: Screen, star: StarData) -> RawTurtle:

    t = RawTurtle(screen.getcanvas())

    t.shape("turtle")
    t.color(star.line_color, star.fill_color)
    t.penup()
    t.setposition(star.pos[0], star.pos[1] + star.size / 2)
    t.pendown()
    t.setheading(270 - star.half_angle)

    return t