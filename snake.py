from turtle import Turtle

distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-20, 0),  (-40, 0)]


class Snake:

    def __init__(self):
        self.objects = []
        self.create_snake()
        self.head = self.objects[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_item(position)

    def add_item(self, position):
        new_object = Turtle("square")
        new_object.color("white")
        new_object.penup()
        new_object.goto(position)
        self.objects.append(new_object)

    def reset(self):
        for obj in self.objects:
            obj.goto(1000, 1000)
        self.objects.clear()
        self.create_snake()
        self.head = self.objects[0]

    def extend(self):
        # add a new item to the snake
        self.add_item(self.objects[-1].position())

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