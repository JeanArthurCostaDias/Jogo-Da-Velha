from turtle import Turtle, Screen
from random import randint, choice
from functools import partial

X_places = []
CPU_places = []
cords_list2 = []

first_row = [(-253.0, 232.0), (-20.0, 240.0), (208.0, 231.0)]
second_row = [(-243.0, 48.0), (-21.0, 51.0), (219.0, 58.0)]
third_row = [(-258.0, -139.0), (-24.0, -141.0), (217.0, -138.0)]

first_column = [(-253.0, 232.0), (-243.0, 48.0), (-258.0, -139.0)]
second_column = [(-24.0, -141.0), (-21.0, 51.0), (-20.0, 240.0)]
third_column = [(208.0, 231.0), (219.0, 58.0), (217.0, -138.0)]

main_diagonal = [(-258.00, -139.00), (-21.0, 51.0), (208.0, 231.0)]
secondary_diagonal = [(-253.0, 232.0), (-21.0, 51.0), (217.0, -138.0)]


def check_win(*args, **kwargs):
    if (all(elem in X_places for elem in main_diagonal)) or (all(elem in X_places for elem in secondary_diagonal)):
        screen.exitonclick()
    elif (all(elem in X_places for elem in first_row)) or (all(elem in X_places for elem in second_row)) or (all(elem in X_places for elem in third_row)):
        screen.exitonclick()
    elif (all(elem in X_places for elem in first_column)) or (all(elem in X_places for elem in second_column)) or (all(elem in X_places for elem in third_column)):
        screen.exitonclick()

    elif (all(elem in CPU_places for elem in main_diagonal)) or (all(elem in CPU_places for elem in secondary_diagonal)):
        screen.exitonclick()
    elif (all(elem in CPU_places for elem in first_row)) or (all(elem in CPU_places for elem in second_row)) or (all(elem in CPU_places for elem in third_row)):
        screen.exitonclick()
    elif (all(elem in CPU_places for elem in first_column)) or (all(elem in CPU_places for elem in second_column)) or (all(elem in CPU_places for elem in third_column)):
        screen.exitonclick()

def x_turtle(t, x, y):
    t.shape("Screenshot_2.gif")
    try:
        X_places.append(t.pos())
        cords_list.remove(t.pos())
    except IndexError:
        screen.exitonclick()
    cpu()


def cpu():
    global cpu_cords
    try:
        cpu_cords = choice(cords_list)
        CPU_places.append(cpu_cords)
    except IndexError:
        screen.exitonclick()
    turtle_cords_dict[cpu_cords].shape("Screenshot_3.gif")
    if len(X_places) > 2:
        check_win()
    try:
        cords_list.remove(cpu_cords)
    except IndexError:
        screen.exitonclick()


main_t = Turtle(visible=False)
screen = Screen()
screen.tracer(False)
screen.addshape("Screenshot_2.gif")
screen.addshape("download (1).gif")
screen.addshape("Screenshot_3.gif")
screen.bgpic(picname="new-tic-tac-toe-1.png")
random_cpu_play = randint(0, 9)
turtle_list = []
cords_list = [(-253.0, 232.0), (-243.0, 48.0), (-258.0, -139.0), (-24.0, -141.0), (-21.0, 51.0), (-20.0, 240.0),
              (208.0, 231.0), (219.0, 58.0), (217.0, -138.0)]

for i in cords_list:
    tim = Turtle(shape="square")
    tim.color("white")
    tim.resizemode("user")
    tim.shapesize(8, 8, 0)
    tim.penup()
    tim.goto(i)
    turtle_list.append(tim)
    tim.onclick(partial(x_turtle, tim))

zipped_things = list(zip(turtle_list, cords_list))
turtle_cords_dict = {cords: turtle for turtle, cords in zipped_things}
check_win()
screen.tracer(True)
screen.mainloop()
