import turtle
turtle.Screen().bgcolor("lightblue")
sc=turtle.Screen()
sc.setup(width=600, height=600)
turtle.title("My Turtle Drawing")
t=turtle.Turtle()
t.color("navy")
t.pensize(3)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
turtle.done()


