"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
from freegames import vector
import math

bird = vector(0, 0)
balls = []
gameSpeed = 1.0
tamanhoBolinha = 1.0

def tap(x, y):
    "Move bird up in response to screen tap."

    if x < -200 or x > 200:
        return print("Nao esta clicando no jogo")

    #A ideia é fazer o bird poder se mover aprox 45 graus na diagonal dependendo da posição do click
    #Quanto mais proximo da borda da tela maior o angulo
    angulo = math.radians(90 - x / 4)

    #30px (original do game) de movimento * direção
    telaX = 30 * math.cos(angulo)
    telaY = 30 * math.sin(angulo)

    up = vector(telaX, telaY)
    bird.move(up)

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    "Draw screen objects."
    global tamanhoBolinha

    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20 * tamanhoBolinha, 'black')

    update()

def move():
    global tamanhoBolinha
    global gameSpeed

    "Update object positions."
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15 * tamanhoBolinha:
            draw(False)
            return

    draw(True)

    #O "goto" indica onde será desenhado o texto
    goto(-200, -180)
    write("Spd:%.f%%" % (gameSpeed * 100), font=("Arial", 12, "normal"))
    goto(-200, -200)
    write("Bol:%.f%%" % (tamanhoBolinha * 100), font=("Arial", 12, "normal"))
    ontimer(move, math.floor(50.0 / gameSpeed))

def gameSpeedSobe():
    global gameSpeed
    if gameSpeed >= 2.0: return 0
    gameSpeed = gameSpeed + 0.1

def gameSpeedDesce():
    global gameSpeed
    if gameSpeed <= 0.3: return 0
    gameSpeed = gameSpeed - 0.1

def bolinhaAumenta():
    global tamanhoBolinha
    tamanhoBolinha = tamanhoBolinha + 0.1

def bolinhaDiminui():
    global tamanhoBolinha
    if tamanhoBolinha <= 0.5: return 0
    tamanhoBolinha = tamanhoBolinha - 0.1

setup(width=420, height=420)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
onkey(gameSpeedSobe, "Up")
onkey(gameSpeedDesce, "Down")
onkey(bolinhaDiminui, "Left")
onkey(bolinhaAumenta, "Right")
listen() #Necessario para que os "onkey" funcionem
move()
done()
