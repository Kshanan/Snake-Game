import turtle
import random
import time


delay=0.1
score=0
high_score=0

#Snake Bodies


#Getting a Screen | Canvas
s=turtle.Screen()
s.title("Snake game")
s.bgcolor("yellow")
s.setup(width=600,height=600)
s.tracer(0)

#Create Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.fillcolor("green")
food.color("red")
food.penup()
food.goto(0,200)

segments = []

#score board
sc=turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score:0 | Highscore:0",align="Center",font=("ds-digital",24,"normal"))


def moveup():
    if head.direction !="down":
        head.direction ="up"
def movedown():
    if head.direction !="up":
        head.direction ="down"
def moveleft():
    if head.direction !="right": 
        head.direction ="left"
def moveright():
    if head.direction !="left":
        head.direction ="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#event handeling - key mappings
s.listen()
s.onkeypress(moveup,"Up")
s.onkeypress(movedown,"Down")
s.onkeypress(moveleft,"Left")
s.onkeypress(moveright,"Right")
s.onkeypress(movestop,"space")

#main loop
while True:
    s.update() #this is to update the screen
    #check collission with border
    if head.xcor()>290:
        head.setx(-290)  
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
                
                
    if head.distance(food) <20:
        #move the food to random place
        x=random.randint(-290,290) 
        y=random.randint(-290,290)
        food.goto(x,y)

        #Add new segment to the head 
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay-=0.001

        #increase the Score
        score+=10

        if score > high_score:
            high_score=score
        sc.clear()
        sc.write("Score : {} High Score : {}".format(score,high_score),align="center",font=("ds-digital",24,"normal"))

    #move the Segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segments 0 to head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
    move()

    #check for collision with the body 
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide Segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score=0
            delay=0.1

            #update the score 
            sc.clear()
            sc.write("Score : {} High Score : {}".format(score,high_score),align="center",font=("ds-digital",24,"normal"))

    time.sleep(delay)
s.mainloop() 
           
