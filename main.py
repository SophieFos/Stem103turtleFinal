from StarFunctions import *
import time

#make and init Screen
screen = Screen()
screen.title("Turtle Stars")

another = True
while another:

    #get the star data
    star = get_input()

    #init the turtle
    t = init_turtle(star)

    #calculate leg length
    leg_length = star.size * math.sin(star.chord_angle * .5)

    #if the path is too long make the turtle faster
    if leg_length * star.num_points > 10_000:
        t.speed(0)  #fastest speed
    elif leg_length * star.num_points > 5_000:
        t.speed(10) #2nd fastest

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

        t.hideturtle()

    # handle six pointed weirdness
    else:
        if leg_length * star.num_points > 25_00:
            t.speed(10)
        #init 2nd turtle
        t2 = RawTurtle(screen.getcanvas())
        t2.width(star.line_width)
        t2.shape("turtle")
        t2.color(star.line_color, star.fill_color)
        t2.teleport(star.pos[0] + (-math.sqrt(3)/2) * (star.size / 2), star.pos[1] + .5 * (star.size / 2))
        t2.setheading(300)

        #init 3rd turtle (infill)
        t3 = RawTurtle(screen.getcanvas())
        t3.hideturtle()
        t3.width(star.line_width)
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

        t.hideturtle()
        t2.hideturtle()

    #stare at your star for 3 seconds
    time.sleep(3)

    another = screen.textinput("Continue?", "Do you want to draw another?")
    another = another.lower() == "yes"

    screen.clearscreen()


#leave the program
screen.bye()
