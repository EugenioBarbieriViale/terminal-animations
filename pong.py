# run this as root or it won't work

import os, time, keyboard

os.system("clear")
w, h = 40, 20

class World:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.player_x = self.w // 2
        self.player_y = self.h - 2

        self.ball_x = 15
        self.ball_y = 4

        self.vx = 1
        self.vy = 1

        self.vp = 2

    def move_player(self):
        if keyboard.is_pressed("Right"):
            self.player_x += self.vp

        if keyboard.is_pressed("Left"):
            self.player_x -= self.vp

        if self.player_x < 0:
            self.player_x = self.w

        if self.player_x > self.w:
            self.player_x = 0

    def check_collision(self):
        if self.ball_x >= self.player_x and self.ball_x <= self.player_x + 3 and self.ball_y == self.player_y:
                return True
        return False

    def move_ball(self):
        self.ball_x += self.vx
        self.ball_y += self.vy

        if self.ball_x < 0 or self.ball_x >= self.w:
            self.vx *= -1
        if self.ball_y < 0:
            self.vy *= -1
        if self.check_collision():
            self.vy *= -1
            self.vx *= -1

    def show(self):
        for j in range(0, self.h):
            for i in range(0, self.w):

                if i == self.player_x and j == self.player_y:
                    print("___", end="")

                if i == self.ball_x and j == self.ball_y:
                    print("0", end="")

                else:
                    print(".", end="")

            print()

    def run(self):
        self.move_player()
        self.move_ball()
        self.show()

obj = World(w,h)

while True:
    if keyboard.is_pressed("Esc") or obj.ball_y > h:
        os.system("clear")
        print("YOU LOST")
        break

    obj.run()

    print("Press keys to move. Press Esc to exit")

    time.sleep(0.1)
    os.system("clear")
