# run this as root or it won't work

import os, time, keyboard

os.system("clear")
w, h = 30, 30

def draw_grid(x, y, w, h):
    for j in range(1, h+1):
        for i in range(1, h+1):
            if i == x and j == y:
                print(" @ ", end="")
            else:
                print("   ", end="")

        print()

x = 10
y = 10

while True:
    draw_grid(x, y, w ,h)

    if keyboard.is_pressed("Up"):
        y -= 1
    if keyboard.is_pressed("Down"):
        y += 1
    if keyboard.is_pressed("Left"):
        x -= 1
    if keyboard.is_pressed("Right"):
        x += 1
    if keyboard.is_pressed("q") or keyboard.is_pressed("Esc"):
        os.system("clear")
        break

    if x < 0:
        x = w
    if x > w:
        x = 0

    if y < 0:
        y = h
    if y > h:
        y = 0

    print("Press keys to move. Press q or Esc to exit")

    time.sleep(0.1)
    os.system("clear")
