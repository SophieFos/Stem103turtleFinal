import math
from StarFunctions import *

#make and init Screen
screen = Screen()
screen.title("Turtle Stars")

#get the star data
star = get_input(screen)

#init the turtle
t = init_turtle(screen, star)

#calculate leg length
if star.num_points % 2:
    chord_angle = (math.tau / star.num_points) * (star.num_points // 2)
else:
    chord_angle = (math.tau / star.num_points) * (star.num_points / 2 - 1)
leg_length = star.size * math.sin(chord_angle/2)

#normal star
if star.num_points != 6:

    if star.is_filled:
        t.begin_fill()

    #draw for loop
    for leg in range(star.num_points):
        t.forward(leg_length)
        t.left(180 - star.half_angle * 2)

    if star.is_filled:
        t.end_fill()

# handle six pointed weirdness
else:
    #init 2nd turtle
    t2 = RawTurtle(screen.getcanvas())
    t2.shape("turtle")
    t2.color(star.line_color, star.fill_color)
    t2.teleport(star.pos[0] + (-math.sqrt(3)/2) * (star.size / 2), star.pos[1] + .5 * (star.size / 2))
    t2.setheading(300)

    #init 3rd turtle (infill)
    t3 = RawTurtle(screen.getcanvas())
    t3.hideturtle()
    t3.color(star.line_color, "white")
    t3.teleport(star.pos[0] - (leg_length  / 3), star.pos[1])
    t3.setheading(300)

    if star.is_filled:
        t.begin_fill()
        t2.begin_fill()
        t3.begin_fill()

    #triangles
    for leg in range(int(star.num_points/2)):
        t.forward(leg_length)
        t2.forward(leg_length)
        t.left(180 - star.half_angle * 2)
        t2.left(180 - star.half_angle * 2)

    #infill
    for leg in range(star.num_points):
        t3.forward(leg_length/3)
        t3.left(60)

    if star.is_filled:
        t.end_fill()
        t2.end_fill()
        t3.end_fill()

#leave the screen up until user clicks
screen.exitonclick()
