from turtle import Turtle

distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.objects = []
        self.create_snake()
        self.head = self.objects[0]

    def create_snake(self):
        x_pos = [0, -20, -40]

        for x in x_pos:
            new_object = Turtle("square")
            new_object.color("white")
            new_object.penup()
            new_object.goto(x, 0)
            self.objects.append(new_object)

    def move(self):
        for obj_num in range(len(self.objects) - 1, 0, -1):
            new_x = self.objects[obj_num - 1].xcor()
            new_y = self.objects[obj_num - 1].ycor()

            self.objects[obj_num].goto(new_x, new_y)

        self.head.forward(distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)