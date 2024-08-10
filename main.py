import time
from snakeresources import Snake, Food, ScoreBoard
from turtle import Screen, Turtle
screen = Screen()
screen.setup(600, 600)
screen.bgpic("img_1.png")
screen.title("SNAKE!")
screen.tracer(0)

food = Food()
snake = Snake()
points = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


end = False

while not end:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        points.increase_score()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        points.update_scoreboard()
        points.refresh_highscore()
        snake.refresh()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            points.update_scoreboard()
            points.refresh_highscore()
            snake.refresh()



screen.exitonclick()
