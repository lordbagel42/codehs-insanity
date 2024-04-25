# Assume Karel starts at 0, 0

x = 0
y = 0
heading = 0
# 0 = east, 1 = south, 2 = west, 3 = north

def turnLeft(amount):
    for i in range(amount):
        turn_left()

def moveAmount(amount):
    for i in range(amount):
        move()

def moveToXY(targetX, targetY):
    global x, y
    if targetY != y:
        if targetY > y:
            difference = targetY - y
            heading = 3
            turnLeft(1)
            moveAmount(difference)
            turnLeft(3)
            heading = 0
            y = targetY
        elif targetY < y:
            difference = y - targetY
            heading = 1
            turnLeft(3)
            moveAmount(difference)
            turnLeft(1)
            heading = 0
            y = targetY
    if targetX != x:
        if targetX > x:
            difference = targetX - x
            heading = 0
            moveAmount(difference)
            x = targetX
        elif targetX < x:
            difference = x - targetX
            heading = 2
            turnLeft(2)
            moveAmount(difference)
            turnLeft(2)
            heading = 0
            x = targetX