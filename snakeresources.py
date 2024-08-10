Positions = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle
import random
LEFT = 180
UP = 90
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in Positions:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle()
        tim.color("blue3")
        tim.shape("square")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_numm in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_numm - 1].xcor()
            new_y = self.segments[seg_numm - 1].ycor()
            self.segments[seg_numm].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() !=  DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def refresh(self):
        for seg in self.segments:
            seg.goto(1000, -1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.refresh()

    def refresh(self):
        self.speed("fastest")
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        with open("Snake_highscore.txt") as data:
            self.highscore = int(data.read())
        self.speed("fastest")
        self.color("black")
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",
                   move=False, align="center", font=("Courier", 30, "bold"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align="center",
                   font=("Courier", 30, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",
                   move=False, align="center", font=("Courier", 30, "bold"))

    def refresh_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

        with open("Snake_highscore.txt", mode="w") as highscore:
            highscore.write(f"{self.highscore}")
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align="center", font=("Courier", 40, "bold"))

