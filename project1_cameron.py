import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to draw a filled triangle (mountain)
def draw_mountain(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.goto(x + width / 2, y + height)
    t.goto(x + width, y)
    t.goto(x, y)
    t.end_fill()

# Draw sun
t.penup()
t.goto(250, 180)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw multiple mountains
mountain_colors = ["dimgray", "gray", "darkslategray"]

for i in range(5):
    x = -450 + i * 200
    y = -100
    width = random.randint(180, 260)
    height = random.randint(150, 250)
    color = random.choice(mountain_colors)
    draw_mountain(x, y, width, height, color)

# Draw grass
t.penup()
t.goto(-450, -100)
t.pendown()
t.color("forestgreen")
t.begin_fill()
t.goto(450, -100)
t.goto(450, -300)
t.goto(-450, -300)
t.goto(-450, -100)
t.end_fill()

# Keep window open
screen.mainloop()