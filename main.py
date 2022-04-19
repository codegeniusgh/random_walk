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


my_turtle.shape("turtle")
my_turtle.pensize(15)

directions = [0,90,180,270]
#Generating random walk

for i in range(200844346546423324):
    my_turtle.setheading(random.choice(directions))
    my_turtle.forward(25)
    my_turtle.color(random_color())


#new_item
#my_turtle.forward(60)

my_screen = Screen()
my_screen.exitonclick()