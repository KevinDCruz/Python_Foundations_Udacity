import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(50)
    brad.color("yellow")
    brad.shape("turtle")
    for i in range(36):
        draw_square(brad)
        brad.right(10)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(50)

    window.exitonclick()

def draw_circle(some_turtle):
    angie.circle(100)

draw_art()