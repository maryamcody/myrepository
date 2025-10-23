import turtle
t=turtle.Turtle()
s=turtle.Screen()
colors=["red","orange","yellow","green","blue","indigo","violet"]
s.bgcolor("black")
s.setup(width=600, height=600)
turtle.title("Colorful Spiral Turtle")
t.speed("fastest")
t.hideturtle()
while True:
    for i in range(200):
        t.pencolor(colors[i % len(colors)])
        t.width(i / 100+ 1)
        t.forward(i)
        t.left(50)
    t.right(239)
    for i in range(200,0,-1):
        t.pencolor("black")
        t.width(i / 100+ 7)
        t.forward(i)
        t.right(59)
turtle.done()