from turtle import Turtle

with open("data.txt")as file:
    content = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.c = 0
        # self.high_score = int(content)
        self.scoreboard()
        self.end()

    def reset_score(self):
        if self.c > int(content):
            with open("data.txt", mode='w')as file1:
                file1.write(f"{self.c}")

        self.c = 0

    def end(self):
        self.penup()
        self.color("red")
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"GAME ENDED", font=("Arial", 32, "normal"), align='center')

    def scoreboard(self):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-10, 270)
        self.clear()
        with open("data.txt") as file:
            content = file.read()
        self.write(f"Score : {self.c}  High-score: {content}", font=("Arial", 12, "normal"), align='center')



