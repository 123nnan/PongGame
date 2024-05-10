from turtle import Turtle
FONT = ('Arial', 50, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.pu()
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-50, 200)
        self.write(f'{self.l_score}', False, 'center', FONT)
        self.goto(50, 200)
        self.write(f'{self.r_score}', False, 'center', FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', FONT)