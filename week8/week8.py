"""
def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F'


test_marks = [95, 90, 89.9, 79.9, 70, 65, 59, 45]

for mark in test_marks:
    print("Grade is:", get_grade(mark))
"""
"""
import turtle
def chooseColor(heigt):  # 't' parametresi kaldırıldı, çünkü kullanılmıyor
    if heigt >= 200:
        return "red"
    elif heigt >= 100:
        return "yellow"
    else:
        return "green"

def drawBar(t, heigt, gap):
    t.penup()
    t.left(90)
    t.forward(heigt + gap)
    t.write("" + str(heigt))
    t.backward(heigt + gap)
    t.right(90)
    t.pendown()

    t.fillcolor(chooseColor(heigt))
    t.begin_fill()
    t.left(90)
    t.forward(heigt)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(heigt)
    t.left(90)
    t.end_fill()

def barChart(data):
    max_heigt = max(data)
    num_bars = len(data)
    border = 10
    gap = (max_heigt + border) / 25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = max_heigt + 4 * border
    wn.setworldcoordinates(-border, -border, right, top)

    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    t.speed(0)
    for heigt in data:
        drawBar(t, heigt, gap)

    wn.exitonclick()

data = [15, 80, 221]
barChart(data)
"""
"""""
import turtle
def chooseColor(heigt):  # 't' parametresi kaldırıldı, çünkü kullanılmıyor
    if heigt >= 200:
        return "red"
    elif heigt >= 100:
        return "yellow"
    else:
        return "green"

def drawBar(t, heigt, gap):
    if heigt >= 0:
        labelY = heigt + gap
    else:
        labelY = gap
    t.penup()
    t.left(90)
    t.forward(labelY)
    t.write("" + str(heigt))
    t.backward(labelY)
    t.right(90)
    t.pendown()

    t.fillcolor(chooseColor(heigt))
    t.begin_fill()
    t.left(90)
    t.forward(heigt)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(heigt)
    t.left(90)
    t.end_fill()

def barChart(data):
    max_heigt = max(data)
    min_heigt = min(data)
    num_bars = len(data)
    border = 10
    gap = (max_heigt + border) / 25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = max_heigt + 4 * border
    bottom =min(min_heigt,0) - border
    wn.setworldcoordinates(-border, -border, right, top)

    t = turtle.Turtle()
    t.color("blue")
    t.pensize(3)
    t.speed(0)
    for heigt in data:
        drawBar(t, heigt, gap)

    wn.exitonclick()

data = [48, 117, -60, -240,160,-110,220]
barChart(data)
"""
def findHypot(a, b):

    return (a ** 2 + b ** 2) ** 0.5

side1 = 3
side2 = 4
print(f"The hypotenuse of a triangle {side1} and {side2} is:", findHypot(side1, side2))





