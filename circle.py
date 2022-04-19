#@codegeniusgh on Twitter
from turtle import Turtle, Screen
import random
import turtle
#import turtle


turtle.colormode(255)#This sets the colormode to 255, so that it can be changed using rgb
#turtle_colors = ["midnight blue","dark green","maroon","olive drab","dark slate blue","purple","dim gray","cadet blue","medium spring green","dark goldenrod"]
my_turtle = Turtle()


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_color = (r,g,b)
    return my_color


my_turtle.speed("fastest")
my_turtle.pensize(5)

#gap_size = 
for i in range(int(360/5)):
    my_turtle.color(random_color())
    my_turtle.circle(200)
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading + 5)

my_screen = Screen()
my_screen.exitonclick()