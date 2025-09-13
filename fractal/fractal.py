import turtle


def koch_segment(t: turtle.Turtle, length: int, depth: int):
    angles = [60, -120, 60, 0]
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        for angle in angles:
            koch_segment(t, length, depth - 1)
            t.left(angle)

def paint_koch(length: int, depth: int):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    for i in range(3):
        koch_segment(t, length, depth)
        t.right(120)
    window.mainloop()

