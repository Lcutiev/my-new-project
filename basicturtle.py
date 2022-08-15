import turtle

# tạo một cái màn hình để mình vẽ
vinh_screen = turtle.Screen()
# vinh_screen.setup(500,500)

# tạo một cây bút ( gọi turtle)
t = turtle.Turtle()

t.pensize(2)
t.pencolor("red")
t.pendown()
t.forward(100)
t.left(90)

t.penup()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# done
turtle.done()