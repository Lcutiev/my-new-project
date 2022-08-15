import turtle
  
t = turtle.Turtle()
  
# for background
screen = turtle.Screen()
screen.bgcolor("light blue")
  
#color and speed
# creating the house
t.color("black")
t.shape("turtle")
t.speed(0)

# the house
t.fillcolor('blue')
t.begin_fill()

l = 90;
m = 250;
n = 400;

t.right(l)
t.forward(m)
t.left(l)


# vẽ cạnh thứ hai
t.forward(n)
t.left(l)
 
# vẽ cạnh thứ ba
t.forward(m)
t.left(l)


# vẽ cạnh thứ tư
t.forward(n)
t.right(l)

t.end_fill()

# top of the house
t.fillcolor('fuchsia')
t.begin_fill()

t.right(45)
t.forward(282)
t.right(90)
t.forward(282)
t.right(45)
 
t.end_fill()

# windows
t.right(90)
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)

t.fillcolor('orange')
t.begin_fill()
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.end_fill()

t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)

# for door
t.right(90)
t.forward(75)
t.left(90)
t.forward(15)
t.left(90)
t.forward(200)
t.right(90)
t.forward(15)
t.right(90)
t.forward(75)

t.fillcolor('yellow')
t.begin_fill()
t.circle(10)
t.end_fill()
t.forward(120)

turtle.done()