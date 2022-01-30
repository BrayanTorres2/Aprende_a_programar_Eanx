gridText = '''
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# . . . . . . . . . . . . # # . . . . . . . . . . . . #
# . # # # # . # # # # # . # # . # # # # # . # # # # . #
# O # # # # . # # # # # . # # . # # # # # . # # # # O #
# . # # # # . # # # # # . # # . # # # # # . # # # # . #
# . . . . . . . . . . . . . . . . . . . . . . . . . . #
# . # # # # . # # . # # # # # # # # . # # . # # # # . #
# . # # # # . # # . # # # # # # # # . # # . # # # # . #
# . . . . . . # # . . . . # # . . . . # # . . . . . . #
# # # # # # . # # # # # . # # . # # # # # . # # # # # #
          # . # # # # # . # # . # # # # # . #          
          # . # #                     # # . #          
          # . # #   # # # _ _ # # #   # # . #          
# # # # # # . # #   #             #   # # . # # # # # #
            .       #             #       .            
# # # # # # . # #   #             #   # # . # # # # # #
          # . # #   # # # # # # # #   # # . #          
          # . # #                     # # . #          
          # . # #   # # # # # # # #   # # . #          
# # # # # # . # #   # # # # # # # #   # # . # # # # # #
# . . . . . . . . . . . . # # . . . . . . . . . . . . #
# . # # # # . # # # # # . # # . # # # # # . # # # # . #
# O # # # # . # # # # # . # # . # # # # # . # # # # O #
# . . . # # . . . . . . . . . . . . . . . . # # . . . #
# # # . # # . # # . # # # # # # # # . # # . # # . # # #
# # # . # # . # # . # # # # # # # # . # # . # # . # # #
# . . . . . . # # . . . . # # . . . . # # . . . . . . #
# . # # # # # # # # # # . # # . # # # # # # # # # # . #
# . # # # # # # # # # # . # # . # # # # # # # # # # . #
# . . . . . . . . . . . . . . . . . . . . . . . . . . #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''
'''
 _______  _______  _______  __   __  _______  __    _ 
|       ||   _   ||       ||  |_|  ||   _   ||  |  | |
|    _  ||  |_|  ||       ||       ||  |_|  ||   |_| |
|   |_| ||       ||       ||       ||       ||       |
|    ___||       ||      _||       ||       ||  _    |
|   |    |   _   ||     |_ | ||_|| ||   _   || | |   |
|___|    |__| |__||_______||_|   |_||__| |__||_|  |__| WITH TURTLE
                   
Created by Matt Spataro 8/24/21
             
"up", "down", "left", and "right" to move.
"d" to enter debug mode. 
"space" to advance a single frame in debug mode. 

Personal Best:
Final Score: 28520
Level: 6
            
'''
import turtle
import random
import math
import time

# INTIALIZE SCREEN AND PACMAN
BOX_SIZE = 14

GAME_OVER = False
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

pacman = turtle.Turtle()
pacman.setheading(0)
pacman.color("yellow")
pacman.penup()
pacman.speed(0)

PACMAN_SPEED = 2.15/20*BOX_SIZE
GHOST_SPEED = 2.0/20*BOX_SIZE
PELLET_DURATION = 5

# REGISTER PAC-MAN SHAPE -----------------------------------------------------

RADIUS = BOX_SIZE*0.75
NUM_PHASES = 6
ORIGINAL_START = 65.0
MOUTH_SIZE = 0.3

startAngle = ORIGINAL_START 
for j in range(NUM_PHASES):

  #center
  points = []
  points.append((0,0-RADIUS*MOUTH_SIZE))

  #circle
  angle = startAngle
  endAngle = 360-startAngle
  while angle <= endAngle:
    #add next set of points
    radians = math.radians(angle)
    x = RADIUS*math.cos(radians)
    y = RADIUS*math.sin(radians)
    points.append((y,x))
    #increment the angle
    if endAngle-10 < angle < endAngle:
      angle = endAngle
    else:
      angle += 10

  #center
  points.append((0,0-RADIUS*MOUTH_SIZE))

  #create shape
  screen.register_shape(str(j),points)
  startAngle -= ORIGINAL_START/(NUM_PHASES-1)

#create list of phases
phases = []
for i in range(NUM_PHASES):
  phases.append(str(i))
for i in range(NUM_PHASES-2,0,-1):
  phases.append(str(i))
  
# REGISTER PAC-MAN DYING ANIMATION --------------------------------------

NUM_PHASES = 60
ORIGINAL_START = 180.0

startAngle = ORIGINAL_START 
for j in range(NUM_PHASES-1, -1, -1):

  #center
  points = []
  points.append((0,0-RADIUS*MOUTH_SIZE))

  #circle
  angle = startAngle
  endAngle = 360-startAngle
  while angle <= endAngle:
    #add next set of points
    radians = math.radians(angle)
    x = RADIUS*math.cos(radians)
    y = RADIUS*math.sin(radians)
    points.append((y,x))
    #increment the angle
    if endAngle-10 < angle < endAngle:
      angle = endAngle
    else:
      angle += 10

  #center
  points.append((0,0-RADIUS*MOUTH_SIZE))

  #create shape
  screen.register_shape("DEATH"+str(j),points)
  startAngle -= ORIGINAL_START/(NUM_PHASES-1)

#create list of phases
death_phases = []
for i in range(NUM_PHASES):
  death_phases.append("DEATH"+str(i))

#REGISTER PAC-DOT SHAPE ------------------------------------------------------

PACDOT_RADIUS = BOX_SIZE/7.5
points = []
for angle in range(0,360,10):
  #add next set of points
  radians = math.radians(angle)
  x = PACDOT_RADIUS*math.cos(radians)
  y = PACDOT_RADIUS*math.sin(radians)
  points.append((y,x))
#create shape
screen.register_shape("pacdot",points)

PELLET_RADIUS = BOX_SIZE/2.5
points = []
for angle in range(0,360,10):
  #add next set of points
  radians = math.radians(angle)
  x = PELLET_RADIUS*math.cos(radians)
  y = PELLET_RADIUS*math.sin(radians)
  points.append((y,x))
#create shape
screen.register_shape("pellet",points)

# JUNI LOGO --------------------------------------------------

def circle(diameter, x, y):
  pen.penup()
  pen.goto(x+diameter/2.0, y+diameter/2.0)
  pen.pendown()
  length = diameter*math.pi/36
  pen.forward(length/2)
  pen.begin_fill()
  for i in range(36):
    pen.right(10)
    pen.forward(length)
  pen.end_fill()

def rectangle(width, height, x, y):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.begin_fill()
  for i in range(2):
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
  pen.end_fill()

def curve(weight, x, y):
  pen.penup()
  pen.goto(x, y)
  pen.pendown()
  pen.setheading(-90)
  length = weight*math.pi/36
  pen.begin_fill()
  for i in range(9):
    pen.forward(length)
    pen.right(10)
  pen.setheading(180)
  pen.forward(weight/2)
  pen.left(90)
  pen.forward(weight)
  pen.left(90)
  pen.forward(weight/2)
  pen.left(90)
  pen.right(90)
  pen.forward(weight/2)
  for i in range(18):
    pen.left(5)
    pen.forward(length)
  pen.forward(weight/2)
  pen.left(90)
  pen.forward(weight)
  pen.end_fill()
  pen.setheading(0)

def cap(weight, x, y):
  pen.penup()
  pen.goto(x, y)
  pen.pendown()
  pen.begin_fill()
  pen.forward(weight)

  # u shape
  pen.right(90)
  length = weight*math.pi/36*1.5
  for i in range(18):
    pen.forward(length)
    pen.left(10)
  pen.forward(length)

  # right post
  pen.right(90)
  pen.forward(weight)
  pen.right(90)
  pen.forward(weight*1.55)
  pen.right(90)
  pen.forward(weight)
  pen.right(90)

  # small curve
  pen.forward(weight-length*2.4)
  pen.right(180)
  for i in range(9):
    pen.right(10)
    pen.forward(length)
  pen.forward(length)

  # large curve
  pen.forward(length)
  for i in range(18):
    pen.right(5)
    pen.forward(length)
  pen.end_fill()
  pen.setheading(0)

def J(weight, height, x, y):
  circle(weight, x, y+weight)
  rectangle(weight, height, x, y)
  curve(weight, x, y-height)

def U(weight, height, x, y):
  rectangle(weight, height, x, y)
  rectangle(weight, height, x+weight*2.5, y)
  cap(weight, x, y-height)
  pen.setheading(0)

def N(weight, height, x, y):
  pen.setheading(180)
  cap(weight, x+weight*3.5, y-weight*1.55)
  rectangle(weight, height, x, y-weight*1.55)
  rectangle(weight, height, x+weight*2.5, y-weight*1.55)

def I(weight, height, x, y):
  circle(weight, x, y+weight)
  rectangle(weight, height+weight*1.55, x, y)

def draw_logo(x, y, weight, height, spacing):
  pen.color(41, 37, 99)
  J(weight, height, x+spacing*0, y)
  U(weight, height, x+spacing*1, y)
  N(weight, height, x+spacing*2 + weight*2.55, y)
  I(weight, height, x+spacing*3 + weight*5.10, y)

#INITALIZE GRID --------------------------------------------------------------

def createGrid(text):
  grid = []
  gridLines = text.strip().split("\n")
  #convert the list into a two-dimensional list
  for i in range(len(gridLines)):
    row = []
    for j in range(0,len(gridLines[0]),2):
      gridLines[i][j].strip()
      row.append(gridLines[i][j])
    grid.append(row)
  return grid
    
grid = createGrid(gridText)

#GRID HELPER FUNCTIONS -----------------------------------------------------

halfGridWidth = int(len(grid[0])/2)
halfGridHeight = int(len(grid)/2)

def updateRowAndColumn(obj):
  obj.row, obj.column = rowAndColumnOf(obj, "CENTER")
  
def rowAndColumnOf(obj, part):
  # get the row and column 
  # based on the object's direction and part
  half = BOX_SIZE/2.0
  x = obj.xcor()
  y = obj.ycor()
  
  if obj.heading() == 0:
    if part == "FRONT":
      x += half
      x -= 1.0 / 20 * BOX_SIZE
    elif part == "BACK":
      x -= half
  elif obj.heading() == 90:
    if part == "FRONT":
      y += half
      y -= 1 / 20 * BOX_SIZE
    elif part == "BACK":
      y -= half
  elif obj.heading() == 180:
    if part == "FRONT":
      x -= half
    elif part == "BACK":
      x += half
      x -= 1 / 20 * BOX_SIZE
  elif obj.heading() == 270:
    if part == "FRONT":
      y -= half
    elif part == "BACK":
      y += half
      y -= 1 / 20 * BOX_SIZE
      
  return rowAndColumn(x, y)

'''
-----------------------------
PYTHON 2 DIVISION
-----------------------------

Integer Division:                 -15 // 10 = -2
Float Division:                  -15.0 / 10 = -1.5
Float Division Cast to Int: int(-15.0 / 10) = -1.0

Integer division will always round "down". This measn we round to a smaller positive number and a bigger negative number.
This is what we want so that we ALWAYS snap to the lower left hand corner of the box (whether positive or negative)

'''
def rowAndColumn(x,y):
  #snap the x and y into the bottom left hand corner of a box
  x = (x // BOX_SIZE) * BOX_SIZE
  y = (y // BOX_SIZE) * BOX_SIZE
  #convert coordinates into indexes
  row = int(halfGridHeight - (y/BOX_SIZE) - 1)
  column = int(halfGridWidth + (x/BOX_SIZE))
  return row, column

def xAndY(row, column):
  # find the bottom left hand corner 
  x = (column - halfGridWidth)*BOX_SIZE 
  y = (-1*row + halfGridHeight - 1)*BOX_SIZE
  # add half of the box size to find the center point
  x += BOX_SIZE/2.0
  y += BOX_SIZE/2.0
  return x, y

# DRAW BOARD --------------------------------------------------------

pen = turtle.Turtle()
pen.speed(0)
pen.ht()
pen.pensize(5)
pen.color("blue")

# NEW ALGORITHM:
def has_top(row,col,grid):
  return row > 0 and grid[row-1][col] == "#"
def has_bottom(row,col,grid):
  return row < len(grid)-1 and grid[row+1][col] == "#"
def has_left(row,col,grid):
  return col > 0 and grid[row][col-1] == "#"
def has_right(row,col,grid):
  return col+1 < len(grid[row]) and grid[row][col+1] == "#"

def get_horizontal_lines(grid):
  lines = []
  for row in range(len(grid)):
    p1 = None
    for col in range(len(grid[row])):
      if grid[row][col] == "#":
        if p1 is None:
          p1 = (row, col)
        if col+1 < len(grid[row]) and grid[row][col+1] == "#":
          if has_top(row,col,grid) and has_bottom(row,col,grid):
            if has_top(row,col+1,grid) and has_bottom(row,col+1,grid):
              p2 = (row, col)
              if p1 != p2:
                lines.append((p1, p2))
              p1 = None
        else:
          p2 = (row, col)
          if p1 != p2:
            lines.append((p1, (row, col)))
          p1 = None
  return lines

def get_vertical_lines(grid):
  lines = []
  for col in range(len(grid[0])):
    p1 = None
    for row in range(len(grid)):
      if grid[row][col] == "#":
        if not p1:
          p1 = (row, col)
        if row+1 < len(grid) and grid[row+1][col] == "#":
          if has_left(row,col,grid) and has_right(row,col,grid):
            if has_left(row+1,col,grid) and has_right(row+1,col,grid):
              p2 = (row, col)
              if p1 != p2:
                lines.append((p1, (row, col)))
              p1 = None
        else:
          p2 = (row, col)
          if p1 != p2:
            lines.append((p1, (row, col)))
          p1 = None
  return lines

# GET GRID LINES
grid_lines = []
grid_lines += get_horizontal_lines(grid)
grid_lines += get_vertical_lines(grid)

left = int(len(grid[0])/2)*BOX_SIZE*-1
right = int(len(grid[0])/2)*BOX_SIZE
top = int(len(grid)/2)*BOX_SIZE
bottom = int(len(grid)/2)*BOX_SIZE*-1

offset = -0.5
topLeft = (0+offset, 0+offset)
topRight = (0+offset, len(grid[0])+offset)
bottomLeft = (len(grid)+offset, 0+offset)
bottomRight = (len(grid)+offset, len(grid[0])+offset)

grid_lines.append((topLeft, topRight))
grid_lines.append((bottomLeft, bottomRight))
grid_lines.append((topLeft, bottomLeft))
grid_lines.append((topRight, bottomRight))

def draw_line(line):
  pen.penup()
  pen.goto(*xAndY(*line[0]))
  pen.pendown()
  pen.goto(*xAndY(*line[1]))
  pen.penup()

def drawBoard(color="blue"):
  global count, complete
  complete = len(grid_lines)
  pen.color(color)
  pen.pensize(4)
  for i in range(len(grid_lines)):
    line = grid_lines[i]
    draw_line(line)
    count += 1
  pen.color("white")
  draw_line(((12,12),(12,15)))

count, complete = 0, 1
while count < complete:
  drawBoard()

def drawBox(x,y):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.setheading(0)
  for i in range(4):
    pen.forward(BOX_SIZE)
    pen.left(90)

def drawDebugGrid():
  global count, complete
  complete = len(grid) * len(grid[0])
  pen.pensize(2)
  for row in range(count // len(grid[0]), len(grid)):
    for column in range(count % len(grid[row]), len(grid[row])): 
      if grid[row][column] == "#":
        x, y = xAndY(row, column) # DEBUG
        pen.color(40,40,40)
        drawBox(x-BOX_SIZE/2.0,y-BOX_SIZE/2.0)
        pen.color("white")
        pen.penup()
        pen.goto(x, y)
        pen.write((row, column),font=("Arial",int(5.0/20*BOX_SIZE)), align="center")
      count += 1
      
#DRAW PACDOTS ----------------------------------------------------------------

pacdots = set()
pellets = set()

#preparing the pen to draw dots
pen.color(255,170,165)
pen.shape("pacdot")
pen.penup()

#function for creating a single pacdot
def addPacDot(row, column):
  x, y = xAndY(row, column)
  pacdots.add((x,y)) 
  
def addPacPellet(row, column):
  x, y = xAndY(row, column)
  pellets.add((x,y)) 

def createPacDots():
  #drawing dots where there is an empty path
  pen.color(255,170,165)
  for row in range(len(grid)-1):
    for column in range(len(grid[0])-1):
      if grid[row][column] == ".":
        addPacDot(row, column)
      if grid[row][column] == "O":
        addPacPellet(row,column)

def drawPacDots():
  global count, complete
  dotlist = list(pacdots)
  complete = len(dotlist)
  pen.color(255,170,165)
  for i in range(count, len(dotlist)):
    x, y = dotlist[i]
    pen.penup()
    pen.goto(x,y)
    pen.shape("pacdot")
    pen.stamp()
    count += 1

createPacDots()
count, complete = 0, 1
while count < complete:
  drawPacDots()
    
# GHOST AI -----------------------------------------------------------------

def possibleDirections(obj):
  d = []
  side1 = (obj.heading()+90)%360
  side2 = (obj.heading()-90)%360
  if not touchingWall(obj, side1):
    d.append(side1)
  if not touchingWall(obj, side2):
    d.append(side2)
  return d

def randomMove(obj):
  # TODO: what do I do if there's a dead end?
  if obj.choice != (obj.row, obj.column):
    
    # "consume" forward move
    if obj.nextDirection == obj.heading():
        obj.nextDirection = "NONE"
    # choose the nextDirection if it's currently NONE
    if obj.nextDirection == "NONE":
      d = possibleDirections(obj)
      if len(d) > 0: # you're at an intersection!
        # add the option of going straight (if possible)
        if not touchingWall(obj, obj.heading()):
          d.append(obj.heading())
        # make a random choice!
        obj.nextDirection = random.choice(d)
        obj.choice = (obj.row, obj.column) # save the cell
      
  # turn and move if possible
  turn(obj)
  if not moveForward(obj):
    obj.nextDirection = "NONE"
    
def smartMove(obj, targetX=None, targetY=None):
  
  # if in a new square after making a choice
  if obj.choice != (obj.row, obj.column):
    
    # "consume" forward move
    if obj.nextDirection == obj.heading():
      obj.nextDirection = "NONE"
      
    # choose the nextDirection
    if obj.nextDirection == "NONE":
      d = possibleDirections(obj)
      if len(d) > 0: # you're at an intersection!
        
        # add the option of going straight
        if not touchingWall(obj, obj.heading()):
          d.append(obj.heading())
        
        if obj.choice == None: 
          # add option of reversing if it's the first time
          reverse = (obj.heading()+180)%360
          if not touchingWall(obj, reverse):
            d.append(reverse)
          
        bestDirections = []
        lowestDistance = 1000000 # positive infinity
        centerX, centerY = xAndY(obj.row, obj.column)
        
        for direction in d:
          x = centerX
          y = centerY
          
          if direction == 0:
            x += BOX_SIZE
          elif direction == 90:
            y += BOX_SIZE
          elif direction == 180:
            x -= BOX_SIZE
          elif direction == 270:
            y -= BOX_SIZE
          
          # manhattan distance
          if targetX is None or targetY is None:
            dist = abs(pacman.xcor()-x) + abs(pacman.ycor()-y)
          else: # with targetX and targetY
            dist = abs(targetX-x) + abs(targetY-y)
          # find smallest
          if dist < lowestDistance:
            lowestDistance = dist
            bestDirections = [direction]
          elif dist == lowestDistance:
             bestDirections.append(direction)
             
        obj.nextDirection = random.choice(bestDirections)
        obj.choice = (obj.row, obj.column)
    
  # turn and move if possible
  turn(obj)
  if not moveForward(obj):
    obj.nextDirection = "NONE"

# TODO: home corners code not yet implemented    
def homeCornerMove(obj):
  if obj.name == "blinky":
    smartMove(obj, *xAndY(1, 1))
  elif obj.name == "pinky":
    smartMove(obj, *xAndY(1, 26))
  elif obj.name == "inky":
    smartMove(obj, *xAndY(29, 1))
  elif obj.name == "clyde":
    smartMove(obj, *xAndY(29, 26))
def headToCorners():
  for ghost in ghosts:
    if ghost.state == "normal" and not ghost.isLeaving:
      ghost.move = bind(homeCornerMove, ghost)
      if ghost.name == "blinky" or ghost.name == "pinky":
        clock.schedule_unique(applyBind(smartMove, ghost), PELLET_DURATION)
      elif ghost.name == "inky" or ghost.name == "clyde":
        clock.schedule_unique(applyBind(randomMove, ghost), PELLET_DURATION)
  
def leaveHouse(obj):
  obj.isLeaving = True
  x, y = xAndY(11, 13.5)
  # line up horizontally
  if obj.xcor() != x:
    # turn
    if obj.xcor() < x:
      obj.setheading(0)
    else:
      obj.setheading(180)
    # move 
    diff = abs(obj.xcor() - x)
    if diff < obj.velocity:
      obj.forward(diff)
    else:
      obj.forward(obj.velocity)
  elif obj.xcor() == x:
    # line it up perfectly
    obj.setheading(90)
    diff = abs(obj.ycor() - y)
    if diff < obj.velocity:
      obj.forward(diff)
    else:
      obj.forward(1.0/20*BOX_SIZE)
    
    # if the ghost fully exited
    if obj.ycor() == y:
      obj.isLeaving = False
      resetGhostMoves(obj)
      return
    
def returnToHouse(obj):
  if not obj.isEntering: # move towards the house
    targetX, targetY = xAndY(11, 13.5)
    smartMove(obj, targetX, targetY) 
    if obj.ycor() == targetY: # correct row
      diff = abs(obj.xcor() - targetX)
      if diff < obj.velocity: # correct column
        obj.forward(diff)
        obj.isEntering = True
  elif obj.isEntering: # perfectly aligned
    obj.setheading(270)
    targetX, targetY = xAndY(14, 13.5)
    if obj.ycor() != targetY:
      diff = abs(obj.ycor() - targetY)
      if diff < obj.velocity:
        obj.forward(diff)
      else:
        obj.forward(1)
    else: # done!
      obj.isEntering = False
      resetGhostLooksAndSpeed(obj)
      clock.schedule_unique(applyBind(leaveHouse, obj), 2)
      
def bind(func, obj):
  obj.nextDirection = "NONE"
  obj.choice = None
  def wrapper():
    func(obj)
  return wrapper
  
def applyBind(func, obj):
  def wrapper():
    obj.move = bind(func, obj)
  return wrapper

# GHOST TRANSITIONS -------------------------------------------------------

def weakMode():
  for ghost in ghosts:
    if ghost.state != "captured":
      ghost.color("#0032ff")
      ghost.state = "weak"
      ghost.adjustment = -GHOST_SPEED/2.0
      if not ghost.isLeaving:
        ghost.setheading((ghost.heading()+180)%360)
        ghost.move = bind(randomMove, ghost)
      
def normalMode():
  pacman.ghostBonus = 200
  for ghost in ghosts:
    if ghost.state != "captured":
      resetGhostLooksAndSpeed(ghost)
      ghost.adjustment = 0
      if not ghost.isLeaving:
        resetGhostMoves(ghost)
  clock.unschedule(blinkGhosts)
  
def capturedMode(ghost):
  # write the ghost bonus
  ghost.color("cyan")
  ghost.sety(ghost.ycor()-BOX_SIZE/2.0)
  ghost.write(str(pacman.ghostBonus), align="center",font=("Arial",int(BOX_SIZE), "bold"))
  ghost.sety(ghost.ycor()+BOX_SIZE/2.0)
  # add ghost score
  pacman.score += pacman.ghostBonus
  pacman.lifePoints += pacman.ghostBonus
  pacman.ghostBonus *= 2
  scoreKeeper.draw(pacman.score)
  # pause for effect
  ghost.ht()
  while clock.wait(1):
    pacman.ht()
    screen.update()
  ghost.st()
  pacman.st()
  ghost.clear()
  # start heading back
  ghost.state = "captured"
  ghost.color("white")
  ghost.shape("pellet")
  ghost.velocity = 9.0/20*BOX_SIZE
  ghost.move = bind(returnToHouse, ghost)

def startGhost(ghost):
  def wrapper():
    ghost.move = bind(leaveHouse, ghost)
    index = ghosts.index(ghost)
    if index < len(ghosts)-1: # start the next ghost
      nextGhost = ghosts[index+1]
      clock.schedule_unique(startGhost(nextGhost), 2)
  return wrapper
  
def touchedPacMan(ghost):
  return abs(ghost.xcor()-pacman.xcor()) < BOX_SIZE*0.75 and abs(ghost.ycor()-pacman.ycor()) < BOX_SIZE*0.75
      
# RESIZABLE --------------------------------------------------------------      
def make_resizable(obj):
  def resize(size):
    shape = obj.shape()
    points = [(point[0]*size,point[1]*size) for point in shapes[shape]] 
    turtle.Screen().register_shape(shape, points)
    obj.shape(shape) #refresh the shape
  def register_shape(name, points):
    shapes[name] = points
    turtle.Screen().register_shape(name, points)
  #bind functions:
  obj.resize = resize
  obj.register_shape = register_shape
  shapes = {
  "turtle": ((0,16),(-2,14),(-1,10),(-4,7),(-7,9),
            (-9,8),(-6,5),(-7,1),(-5,-3),(-8,-6),
            (-6,-8),(-4,-5),(0,-7),(4,-5),(6,-8),
            (8,-6),(5,-3),(7,1),(6,5),(9,8),(7,9),
            (4,7),(1,10),(2,14))}

# CREATE GHOSTS -----------------------------------------------------------

blinky = turtle.Turtle()
pinky = turtle.Turtle()
inky = turtle.Turtle()
clyde = turtle.Turtle()
blinky.rgb = (255, 0, 0)
pinky.rgb = (255, 184, 222)
inky.rgb = (0, 255, 222)
clyde.rgb = (255, 184, 71)
blinky.name = "blinky"
pinky.name = "pinky"
inky.name = "inky"
clyde.name = "clyde"
ghosts = [blinky, pinky, inky, clyde]
for ghost in ghosts:
  ghost.speed(0)
  ghost.penup()
  updateRowAndColumn(ghost)
  ghost.isLeaving = False
  ghost.isEntering = False

# -8-16 y range
# -9-9 x range
# 18 is the entire width of the regular sized turtle (9+9)
# multiply by 1.5 so that it's the same size as pacman
def resetGhostLooksAndSpeed(ghost):
  ghost.velocity = GHOST_SPEED
  ghost.adjustment = 0
  ghost.state = "normal"
  ghost.shape("turtle")
  make_resizable(ghost)
  # range of original is 18 pixels
  ghost.resize((BOX_SIZE/18.0)*1.5) 
  ghost.color(ghost.rgb)
  
def resetGhostMoves(ghost):
  if ghost.name == "blinky" or ghost.name == "pinky":
    ghost.move = bind(smartMove, ghost)
  elif ghost.name == "inky" or ghost.name == "clyde":
    ghost.move = bind(randomMove, ghost)
  else:
    raise "Unknown Name of Ghost"

def resetGhosts():
  blinky.goto(*xAndY(14, 12))
  clyde.goto(*xAndY(14, 15))
  inky.goto(*xAndY(14, 14))
  pinky.goto(*xAndY(14, 13))
  for ghost in ghosts:
    ghost.st()
    ghost.setheading(90)
    ghost.isEntering = False
    resetGhostLooksAndSpeed(ghost)
    resetGhostMoves(ghost)
resetGhosts()

# PORTALS -----------------------------------------------------------

box = ((-BOX_SIZE, BOX_SIZE), (BOX_SIZE, BOX_SIZE), (BOX_SIZE, -2*BOX_SIZE), (-BOX_SIZE, -2*BOX_SIZE))
turtle.Screen().register_shape("box", box)

leftPortal = turtle.Turtle()
leftPortal.color("black")
leftPortal.shape("box")
leftPortal.penup() 
leftPortal.goto(*xAndY(14,-1.25))
leftPortal.stamp()
leftPortal.goto(*xAndY(14,-1.75))

rightPortal = turtle.Turtle()
rightPortal.color("black")
rightPortal.shape("box")
rightPortal.penup() 
rightPortal.goto(*xAndY(14,29.25))
rightPortal.stamp()
rightPortal.goto(*xAndY(14,29.75))

# EVENT LISTENERS ------------------------------------------------------

def pressUp():
  pacman.nextDirection = 90
def pressDown():
  pacman.nextDirection = 270
def pressLeft():
  pacman.nextDirection = 180
def pressRight():
  pacman.nextDirection = 0
  
def printSpeeds():
  for ghost in ghosts:
    print(ghost.name, ghost.velocity, ghost.adjustment)
  print(pacman.name, pacman.velocity, pacman.adjustment)
  
paused = False
def step():
  global paused
  paused = False
  
debugMode = False
drawing = False
def debug():
  global debugMode, paused, count, complete, drawing
  if not GAME_OVER and not drawing:
    drawing = True
    debugMode = not debugMode
    pen.clear()
    if debugMode:
      count, complete = 0, 1
      while count < complete:
        drawDebugGrid()
      count, complete = 0, 1
      while count < complete:
        drawPacDots()
    else:
      count, complete = 0, 1
      while count < complete:
        drawBoard()
      count, complete = 0, 1
      while count < complete:
        drawPacDots()
      paused=False
    drawing = False
    
screen.onkey("up",pressUp)
screen.onkey("down", pressDown)
screen.onkey("left", pressLeft)
screen.onkey("right", pressRight)
screen.onkey("d", debug)
screen.onkey("space", step)
screen.onkey("s",printSpeeds)
screen.listen()

# MOVING AND TURNING  ----------------------------------------------------

'''
aligns the given object in the direction it's moving
returns -1 if not aligned
returns the offset if aligned (or close to being aligned)
'''
def align(obj):
  direction = obj.heading();
  offset = -1
  x = obj.xcor()
  y = obj.ycor()
  half = (BOX_SIZE/2.0)
  
  if direction == 0:
    offset = (x+half) % BOX_SIZE
    offset = (BOX_SIZE-offset) % BOX_SIZE
  elif direction == 180:
    offset = (x+half) % BOX_SIZE
  elif direction == 90:
    offset = (y+half) % BOX_SIZE
    offset = (BOX_SIZE-offset) % BOX_SIZE
  elif direction == 270:
    offset = (y+half) % BOX_SIZE
  else:
    raise "ERROR: invalid direction"
    
  if offset < obj.velocity:
    return offset
  else:
    return -1

walls = ["#", "_"]

def touchingWall(obj, direction):
  row, column = obj.row, obj.column #rowAndColumnOf(obj, part)

  # touching walls for portals
  if row == 14 and (column-1 < 0 or column+1 >= len(grid[0])):
    if direction == 0 or direction == 180:
      return False # not touching left and right
    else:
      return True # always touching up and down
  
  if direction == 0:
    return (column+1) >= len(grid[0]) or grid[row][column+1] in walls
  elif direction == 90:
    return (row-1) < 0 or grid[row-1][column] in walls
  elif direction == 180:
    return (column-1) < 0 or grid[row][column-1] in walls
  elif direction == 270:
    return (row+1) >= len(grid) or grid[row+1][column] in walls
  else:
    return False
  
def canTurn(obj):
  if obj.nextDirection == "NONE" or obj.nextDirection == obj.heading():
    return False
  if not touchingWall(obj, obj.nextDirection):
    if (obj.nextDirection + 180) % 360 == obj.heading():
      return True
    offset = align(obj)
    if offset >= 0:
      obj.forward(offset)
      return True
  return False
  
def canMove(obj):
  if touchingWall(obj,obj.heading()):
    offset = align(obj)
    if offset >= 0:
      obj.forward(offset)
      return False
  return True
  
def turn(obj):
  if canTurn(obj):
    obj.setheading(obj.nextDirection)
    obj.nextDirection = "NONE"
    if obj.name == "pacman": 
      # slightly faster around corners
      moveForward(obj) 
      moveForward(obj)
  
def moveForward(obj):
  if canMove(obj):
    if obj.name == "pacman":
      obj.forward(obj.velocity+obj.adjustment)
    else:
      if obj.state != "captured" and obj.row == 14 and (obj.column < 3 or obj.column > 24):
        obj.forward(1.0/20*BOX_SIZE) # ghosts slow through portals
      else:
        obj.forward(obj.velocity+obj.adjustment)
    # portal code
    if obj.xcor() <= leftPortal.xcor():
      obj.setx(rightPortal.xcor())
    elif obj.xcor() > rightPortal.xcor():
      obj.setx(leftPortal.xcor())
    return True
  return False
  
def eatPacDot():
  row, column = rowAndColumnOf(pacman, "BACK")
  x, y = xAndY(row, column)
  pen.penup()
  pen.goto(x,y)
  pen.color("black")
  
  if (x, y) in pacdots or (x, y) in pellets:
    gridCopy[row][column] = " "
    pacman.previous = (row, column)
    pacman.adjustment = -0.30/20*BOX_SIZE
  elif pacman.previous != (row, column) and row >= 0 and row < len(grid) and column >=0 and column < len(grid[row]) and gridCopy[row][column] == " ":
    pacman.adjustment = 0

  if (x, y) in pacdots:
    pen.stamp()
    pacdots.remove((x, y))
    pacman.score += 10
    pacman.lifePoints += 10
    scoreKeeper.draw(pacman.score)
  elif (x, y) in pellets:
    for i in range(10):
      pen.stamp() # stamp multiple times to erase the outline
    pellets.remove((x, y))
    pacman.score += 50
    pacman.lifePoints += 50
    scoreKeeper.draw(pacman.score)
    weakMode()
    clock.schedule_unique(normalMode, PELLET_DURATION)
    clock.schedule_interval(blinkGhosts, PELLET_DURATION/20.0)

# BLINKING ----------------------------------------------------------------   

def blinkGhosts():
  if normalMode in clock.events:
    start = clock.events[normalMode]["start"]
    duration = clock.events[normalMode]["duration"]
    elapsed = time.time()-start
    remaining = duration-elapsed
    if remaining < 2.0:
      for ghost in ghosts:
        if ghost.state == "weak":
          if ghost.color()[0] == "white":
            ghost.color("#0032ff")
          else:
            ghost.color("white")

pelletBlink = 0
def blinkPellets():
  global pelletBlink
  pen.shape("pellet")
  if pelletBlink % 2 == 0:
    pen.color("black")
  else:
    pen.color(255,170,165)
  pen.penup()
  for pellet in pellets:
    pen.goto(pellet[0], pellet[1])
    pen.stamp()
  pelletBlink += 1
  
boardBlink = 0
def blinkBoard():
  global boardBlink
  if boardBlink % 2 == 0:
    drawBoard("white")
  else:
    drawBoard("blue")
  boardBlink += 1

# CLOCK ------------------------------------------------------------------

class Clock():
  def __init__(self):
    self.events = {} # event: info
    self.startTime = None
  def reset(self):
    self.events = {}
    self.startTime = None
  def schedule_unique(self, event, duration):
    self.events[event] = {
      "start": time.time(),
      "duration": duration, 
      "isUnique?":True}
  def schedule_interval(self, event, duration):
    self.events[event] = {
      "start": time.time(),
      "duration": duration, 
      "isUnique?":False}
  def unschedule(self, event):
    if event in self.events:
      self.events.pop(event)
  def wait(self, duration):
    if not self.startTime:
      self.startTime = time.time()
    if time.time()-self.startTime < duration:
      return True
    else: # done with wait
      self.startTime = None
      for event in self.events:
        if self.events[event]["isUnique?"]:
          self.events[event]["duration"] += duration
      return False
  def do_events(self):
    for event in self.events:
      if event in self.events: # to avoid unschedule bug
        start = self.events[event]["start"]
        duration = self.events[event]["duration"]
        if time.time()-start >= duration:
          event()
          if self.events[event]["isUnique?"]:
            self.events.pop(event)
          else:
            self.events[event]["start"] = time.time()
            
# roughly 0.0167 seconds for each game loop 
clock = Clock() 

# STATE TRANSITIONS ---------------------------------------------------------

def startNewRound():
  global paused
  pen.shape("pellet")
  pacman.name = "pacman"
  pacman.adjustment = 0
  pacman.previous = None
  pacman.nextDirection = "NONE"
  pacman.ghostBonus = 200
  pacman.phase = 0
  pacman.goto(0*BOX_SIZE,-8.5*BOX_SIZE)
  pacman.shape(phases[5])
  pacman.setheading(180)
  pacman.velocity = PACMAN_SPEED

  scoreKeeper.draw(pacman.score)
  livesKeeper.draw(pacman.lives)
  levelKeeper.draw(pacman.level)
  resetGhosts()

  # annoucement
  announcer.write("READY!", align="center",font=("Arial",int(BOX_SIZE), "bold"))
  while clock.wait(2):
    pacman.st()
    screen.update()
  announcer.clear()
  paused = False
  
  clock.reset()
  clock.schedule_unique(startGhost(blinky), 2)
  clock.schedule_interval(blinkPellets, 0.25)
  #clock.schedule_interval(headToCorners, 5)
      
def gameOver():
  global GAME_OVER
  GAME_OVER = True
  clock.reset()
  pen.clear()
  for ghost in ghosts:
    ghost.ht()
  pacman.ht()
  screen.update()

gridCopy = createGrid(gridText)
def nextLevel():
  global PACMAN_SPEED, GHOST_SPEED, PELLET_DURATION, gridCopy
  pacman.level += 1
  # increase the speed
  if PACMAN_SPEED + 0.5/20*BOX_SIZE <= 5.15/20*BOX_SIZE:
    PACMAN_SPEED += 0.5/20*BOX_SIZE
    GHOST_SPEED += 0.5/20*BOX_SIZE
  #decrease the duration
  if PELLET_DURATION > 2:
    PELLET_DURATION -= 0.5
  
def lifeLost():
  global paused
  paused = True
  # pause for dramatic effect
  while clock.wait(0.5):
    pacman.st()
    screen.update()
  for ghost in ghosts:
    ghost.ht()
  # death animation
  for phase in death_phases:
    pacman.shape(phase)
    screen.update()
  pacman.ht()
  # update lives
  pacman.lives -= 1
  livesKeeper.draw(pacman.lives)
  if pacman.lives > 0:
    startNewRound()
  else:
    gameOver()

#FINAL INIT ----------------------------------------------------------------

announcer = turtle.Turtle()
announcer.speed(0)
announcer.ht()
announcer.penup()
announcer.color("yellow")
announcer.goto(*xAndY(17.5, 13.5))
  
def createKeeper(title, row, column, align="left"):
  keeper = turtle.Turtle()
  keeper.speed(0)
  keeper.ht()
  keeper.penup()
  keeper.color("white")
  keeper.goto(*xAndY(row, column))
  def draw(value):
    keeper.clear()
    keeper.write(title+str(value), align=align,font=("Arial", int(BOX_SIZE), "bold"))
  keeper.draw = draw
  return keeper
  
scoreKeeper = createKeeper("SCORE: ", -1, 0, "left")
livesKeeper = createKeeper("LIVES: ", -1, 27, "right")
levelKeeper = createKeeper("LEVEL: ", -1, 13.5, "center")
pacman.lifePoints = 0
pacman.score = 0
pacman.lives = 3
pacman.level = 1

# GAME LOOP ------------------------------------------------------------------

startNewRound()

while True:
  if not paused:
    # pacman stuff
    updateRowAndColumn(pacman)
    turn(pacman)
    if moveForward(pacman): # animate if pacman moves
      pacman.shape(phases[pacman.phase])
      pacman.phase = (pacman.phase + 1) % len(phases)
    
    # eat pacdot
    eatPacDot()
      
    # ghost stuff
    for ghost in ghosts:
      updateRowAndColumn(ghost)
      ghost.move()
      if touchedPacMan(ghost):
        if ghost.state == "weak":
          capturedMode(ghost)
        elif ghost.state == "normal":
          lifeLost()
          
    # check for next level or game over
    if len(pacdots) == 0: #and len(pellets) == 0:
      nextLevel()

      # hide ghosts
      for ghost in ghosts:
        ghost.ht()

      # blink the board
      for i in range(6):
        t1 = time.time()
        count, complete = 0, 1
        while count < complete:
          blinkBoard()
        t2 = time.time()
        while time.time()-t1 < 0.5-(t2-t1):
          pacman.st()
          screen.update()

      gridCopy = createGrid(gridText)
      createPacDots()

      # draw pacdots
      count, complete = 0, 1
      while count < complete:
        drawPacDots()

      startNewRound()
    elif GAME_OVER:
      break
        
    # do all timed events
    clock.do_events()
  
  # pause if in debug mode
  if debugMode:
    paused = True
  
  # extra life every 10000 points!
  if pacman.lifePoints >= 10000:
    pacman.lifePoints %= 10000
    pacman.lives += 1
    livesKeeper.draw(pacman.lives)
  
  #update
  scoreKeeper.ht() # avoids crashing
  screen.update()

# GAME OVER ------------------------------------------
scoreKeeper.clear()
livesKeeper.clear()
levelKeeper.clear()

leftPortal.ht()
rightPortal.ht()
leftPortal.clear()
rightPortal.clear()

scoreKeeper.goto(0, 150)
scoreKeeper.write("Final Score: "+str(pacman.score)+"\tLevel: "+str(pacman.level), align="center",font=("Arial",20, "bold"))

# write dedication
pen.penup()
pen.goto(0, 125)
pen.color("white")
pen.write("Created by Matt Spataro for Juni Learning", align="center",font=("Arial",15, "bold"))

draw_logo(-150, 50, weight=30, height=75, spacing=50)

pen.penup()
pen.color("white")
pen.goto(0, -125)
pen.write("We teach kids how to code!", align="center",font=("Arial",15, "bold"))
pen.goto(0, -150)
pen.write("Check us out at junilearning.com", align="center",font=("Arial",15, "bold"))
screen.update()
