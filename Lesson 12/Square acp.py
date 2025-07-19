import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color

# Create a turtle object
t = turtle.Turtle()
t.color("red")  # Pen color
t.pensize(3)    # Pen thickness
t.speed(2)      # Drawing speed

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Draw the square
draw_square(150)

# Finish
turtle.done()
