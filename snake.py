from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body,left_key,right_key,up_key,down_key):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("red")
    self.penup()
    self.setheading(90)
    self.shape("square")
    self.alive = True
    self.st()
    screen.onkeypress(self.left, left_key)
    screen.onkeypress(self.right, right_key)
    screen.onkeypress(self.up, up_key)
    screen.onkeypress(self.down, down_key)
    body.append(self)

  def up(self):
    self.setheading(90)

  def down(self):
    self.setheading(270)

  def left(self):
    self.setheading(180)

  def right(self):
    self.setheading(0)

  def destroy(self):
       self.hideturtle()
       self.alive = False

  def move(self):
        self.forward(20)
        if self.xcor() > 240 or self.xcor() < -240:
          self.destroy()
        if self.ycor() > 240 or self.ycor() < -240:
            self.destroy()
        
        
        
    


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("green")
    self.penup()
    self.setheading(90)
    self.shape("square")
    self.alive = True
    self.st()
    
    self.last = body[-1]
    self.goto(self.last.xcor(),self.last.ycor())

  def move(self):
     self.goto(self.last.xcor(),self.last.ycor())



class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.speed(0)
    self.color("red")
    self.shape("circle")
    self.goto(random.randint(-220,220),random.randint(-220,220))

  def relocate(self): 
    self.goto(random.randint(-220,220),random.randint(-220,220))
    body.append(Segment(p1))
 

def update():
  if p1.alive:
    for i in range(len(body)-1,-1,-1):
      body[i].move()
    if p1.distance(apple) < 30:
      apple.relocate()
    for segment in body[3:len(body)-1:1]:
      if segment.distance(p1) < 10:
        p1.destroy() 
  screen.ontimer(update, 120)

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []


playing_area()

p1 = Head(screen,body,"Left","Right","Up","Down" )

apple = Apple()

update()






screen.exitonclick()
