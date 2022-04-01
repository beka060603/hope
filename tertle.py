import turtle

n = 0
a = 0

turtle.bgcolor('black')
turtle.speed(100)
turtle.pencolor('#ff4040')
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.shape("turtle")
turtle.fd(100)

while 1:
    turtle.forward(n)
    turtle.right(a)
    n += 3
    a += 1
    if a == 200:
        break

turtle.done()
