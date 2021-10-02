import turtle
import time

# Window
wn = turtle.Screen()
wn.title("ching chong by AnNgu")
wn.bgcolor("white")
wn.setup(width=800, height=640)
wn.tracer(0)

# Objects
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.penup()
paddle_a.goto(-320, 0)
paddle_a.shapesize(stretch_wid=4, stretch_len=1)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(320, 0)
paddle_b.shapesize(stretch_wid=4, stretch_len=1)

ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("black")
ball1.penup()
ball1.goto(0, 0)
ball1.shapesize(stretch_wid=1, stretch_len=1)
ball1.dx = 0.15
ball1.dy = -0.15

ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("black")
ball2.penup()
ball2.goto(0, 0)
ball2.shapesize(stretch_wid=1, stretch_len=1)
ball2.dx = -0.125
ball2.dy = -0.125

ball3 = turtle.Turtle()
ball3.speed(0.5)
ball3.shape("circle")
ball3.color("black")
ball3.penup()
ball3.goto(0, 0)
ball3.shapesize(stretch_wid=1, stretch_len=1)
ball3.dx = -0.15
ball3.dy = 0.15

ball4 = turtle.Turtle()
ball4.speed(0.5)
ball4.shape("circle")
ball4.color("black")
ball4.penup()
ball4.goto(0, 0)
ball4.shapesize(stretch_wid=1, stretch_len=1)
ball4.dx = 0.125
ball4.dy = 0.125

balls = [ball1, ball2, ball3, ball4]

t = turtle.Turtle()
t.speed(0)
t.color("black")
t.penup()
t.hideturtle()
t.goto(0, 250)
t.write("Player A: 0 Player B: 0", align="center", font=("Courier", 20, "bold"))
score_a = 0
score_b = 0

# Function
def paddle_a_up():
	paddle_a.sety(paddle_a.ycor() + 30)
	if paddle_a.ycor() > 255:
		paddle_a.sety(paddle_a.ycor() - 30)

def paddle_a_down():
	paddle_a.sety(paddle_a.ycor() - 30)
	if paddle_a.ycor() < -255:
		paddle_a.sety(paddle_a.ycor() + 30)

def paddle_b_down():
	paddle_b.sety(paddle_b.ycor() - 30)
	if paddle_b.ycor() < -255:
		paddle_b.sety(paddle_b.ycor() + 30)

def paddle_b_up():
	paddle_b.sety(paddle_b.ycor() + 30)
	if paddle_b.ycor() > 255:
		paddle_b.sety(paddle_b.ycor() - 30)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Game loop
win = False
while win == False:
	wn.update()
	for ball in balls:
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)
		if ball.ycor() > 270:
			ball.dy *= -1
		if ball.ycor() < -270:
			ball.dy *= -1
		if ball.xcor() > 370:
			ball.goto(0, 0)
			ball.dx *= -1
			score_a += 1
			t.clear()
			t.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
		if ball.xcor() < -370:
			ball.goto(0, 0)
			ball.dx *= -1
			score_b += 1
			t.clear()
			t.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "bold"))
		if (ball.xcor() > 305 and ball.xcor() < 315 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40)):
			ball.setx(305)
			ball.dx *= -1
		if (ball.xcor() < -305 and ball.xcor() > -315 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40)):
			ball.setx(-305)
			ball.dx *= -1
		if score_a == 5:
			t.clear()
			t.goto(0,0)
			t.write("Player B sucks", align="center", font=("Courier", 50, "bold"))
			time.sleep(2)
			win = True
		if score_b == 5:
			t.clear()
			t.goto(0,0)
			t.write("Player A sucks", align="center", font=("Courier", 50, "bold"))
			time.sleep(2)
			win = True
	clstballa = balls[0]
	clstballb = balls[0]
	for ball in balls:
		if ball.xcor() > clstballb.xcor():
			clstballb = ball
		if ball.xcor() < clstballa.xcor():
			clstballa = ball
	if clstballb.xcor() > 200: 
		if paddle_b.ycor() < clstballb.ycor() and abs(paddle_b.ycor() - clstballb.ycor()) > 20:
			paddle_b_up()
		elif paddle_b.ycor() > clstballb.ycor() and abs(paddle_b.ycor() - clstballb.ycor()) > 20:
			paddle_b_down()
	# if clstballa.xcor() < -200:
	# 	if paddle_a.ycor() < clstballa.ycor() and abs(paddle_a.ycor() - clstballa.ycor()) > 20:
	# 		paddle_a_up()
	# 	elif paddle_a.ycor() > clstballa.ycor() and abs(paddle_a.ycor() - clstballa.ycor()) > 20:
	# 		paddle_a_down()