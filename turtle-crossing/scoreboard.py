from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.game_level = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 265)
        self.write("LEVEL :", align = "center", font= FONT)
        self.goto(10, 265)
        self.write(self.game_level, align = "center", font= FONT)

    def increase_score(self):
        self.game_level += 1
        self.update_scoreboard()
