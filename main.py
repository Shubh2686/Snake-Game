from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.down, key="Down")

num = 0
is_game_on = True
while is_game_on:
    screen.update()
    score.scoreboard()
    time.sleep(0.1)
    snake.last_white()
    snake.move()
    if snake.turtle_list[0].distance(food) < 15:
        food.refresh()
        snake.add_turtle()
        score.c += 1
    if snake.wall_check() or snake.tail_check():
        # is_game_on = False
        score.reset_score()
        snake.snake_reset()
        # score.end()

screen.exitonclick()
