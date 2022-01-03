from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]
        self.add_turtle()
        self.last_white()
        self.wall_check()
        self.tail_check()


    def tail_check(self):
        for i in range(1, len(self.turtle_list)):
            if self.turtle_list[0].distance(self.turtle_list[i]) < 10:
                return True

    def snake_reset(self):
        for turtle in self.turtle_list:
            turtle.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]






    def wall_check(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        else:
            return False

    def last_white(self):
        self.turtle_list[-1].color("white")

    def add_turtle(self):
        self.turtle_list.append(Turtle("square"))
        self.turtle_list[-1].penup()
        self.turtle_list[-1].speed("fastest")

    def create_snake(self):
        for p in POSITION:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(p)
            self.turtle_list.append(new_turtle)

    def up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)

    def left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)

    def right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)

    def down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)

    def move(self):
        for i in range(len(self.turtle_list)-1):
            self.turtle_list[-1-i].goto(self.turtle_list[-2-i].pos())
        self.head.forward(STEP)
