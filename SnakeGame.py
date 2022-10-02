from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detecting Collision with he food

    if snake.head.distance(food) < 17:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290:
        game_on = False
        score.game_over()
    if snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_on = False
        score.game_over()
   
   ### Collision with tail
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 18:
            game_on = False
            score.game_over()




screen.exitonclick()