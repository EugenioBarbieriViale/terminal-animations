# run this as root or it won't work

import os, time, keyboard

os.system("clear")
w, h = 50, 24

class World:
    def __init__(self, w, h, dx, dy):
        self.w = w
        self.h = h
    
        self.x = self.w // 2
        self.y = self.h // 2

        self.dx = dx
        self.dy = dy


    def draw(self):
        for j in range(0, self.h):
            for i in range(0, self.w):
                if (i > self.dx and i < self.w - self.dx) and j > self.dy and j < self.h - self.dy: 
                    print("#", end="")

                elif i == 0 or i == self.w-1:
                    print("*", end="")

                else:
                    print(" ", end="")

            print()

    def run(self):
        self.draw()

obj = World(w,h, 18, 8)

while True:
    if keyboard.is_pressed("Esc"):
        os.system("clear")
        break

    obj.run()

    print("Press Esc to exit")

    time.sleep(0.1)
    os.system("clear")
