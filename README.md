# Stem103turtleFinal

## Programmer Info

 Author: Sophie Foslien\
 Course: STEM&103\
 Date: May 7th 2025
 
## Project Description

Opens a Turtle window and uses prompted user-data to draw a star

## Testing

 - Center positions in all four quadrants
 - Size: 1, 0, -100000, reasonable sizes
 - Point number: 0, 5, **6**, 10, 15, 20, 45
 - line_color: green, blue, red, fuchsia, invalid color strings
 - is_filled : true and false for normal and **6** pointed triangles
 - fill_color: same as line color

## Reflection

  - What you learned overall.
  - The new Python feature or concept you explored.
  - Challenges you faced and how you overcame them.

For this project I learned a lot about Turtle, the window manager underneath it, how to  make C like data structs and that composite-number-pointed stars are weird. The new Python features I utilized were the turtle API and dataclasses. I found that to draw an n-pointed star with one stroke, the point index of the second drawn point must be coprime with n.
