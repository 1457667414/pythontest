import turtle

aj = turtle.Pen()
y = 0
aj.speed(5)
# turtle.screensize(200,800)
turtle.bgcolor("black")


# aj.shape("turtle")
def head():
    aj.color("green")
    aj.fd(160)
    x = aj.xcor()
    aj.seth(90)
    aj.begin_fill()
    # aj.color("green")
    aj.circle(x / 2, 180)
    aj.end_fill()
    aj.penup()
    aj.goto(33, 37)
    aj.pendown()
    aj.dot(13, "black")
    aj.penup()
    aj.goto(126, 37)
    aj.pendown()
    aj.dot(13, "black")
    aj.penup()
    aj.home()
    aj.pendown()
    aj.hideturtle()
    aj.fd(160)
    aj.seth(90)
    aj.circle(x / 2, 60)
    aj.right(90)
    aj.pensize(5)
    aj.fd(30)

    aj.penup()
    aj.home()
    # aj.pendown()
    aj.hideturtle()
    aj.fd(160)
    aj.seth(90)
    aj.circle(x / 2, 120)
    aj.right(90)
    aj.pensize(5)
    aj.pendown()
    aj.fd(30)
    aj.penup()
    aj.home()
    aj.penup()


def body():
    aj.pensize(0)

    aj.home()
    aj.showturtle()
    aj.goto(0, -7)
    aj.pendown()
    aj.begin_fill()
    aj.fd(160)
    aj.right(90)
    aj.fd(120)
    aj.right(90)
    aj.fd(160)
    y = aj.ycor()
    aj.right(90)
    aj.fd(120)
    aj.end_fill()


def legs():
    aj.penup()
    # turtle.color("red")
    aj.goto(33, -169)
    aj.pendown()
    aj.pensize(32)
    aj.fd(43)
    aj.penup()
    aj.goto(130, -169)
    aj.pendown()
    aj.fd(43)
    aj.penup()


head()
body()
legs()
turtle.done()
