#!/usr/bin/python
from sense_hat import SenseHat

sh = SenseHat()
sh.set_rotation(180)

levels = {}
pitch  = 0
roll   = 0

red    = (255,0,0)
orange = (255,196,0)
blue   = (0,0,255)
green  = (0,0,0)     # Use these values to set the background
color  = green

RIGHT    = False
ROLL     = False
rowNr    = 0
rowStart = 0
rowLast  = 0
rowDraw  = 0
rowColor = green

TAIL     = False
PITCH    = False
colNr    = 0
colStart = 0
colLast  = 0
colDraw  = 0
colColor = green

def setImuConfig():
    sh.set_imu_config(True, True, True)

def getOrientation():
    global levels, pitch, roll
    
    levels = sh.get_orientation_degrees()
    pitch = int(levels['pitch'])
    roll = int(levels['roll'])
   
def getCompass():
    global heading

    bearing = sh.get_compass() # disables gyro en accelerometer!
    heading = int(bearing)

def drawCol():
    global colDraw, color

    y = 0
    while (y <= 7):
        sh.set_pixel(colDraw,y,color)
        y +=1

def drawRow():
    global rowDraw, color

    x = 0
    while (x <= 7):
        sh.set_pixel(x,rowDraw,color)
        x +=1

def calcLines():
    global pitch, TAIL,  colStart, colNr, PITCH, colColor, \
           roll,  RIGHT, rowStart, rowNr, ROLL,  rowColor

    if pitch >= 270:
        TAIL = True
        pitch = 360 - pitch
        colStart = 4
    else:
        colStart = 3

    if pitch > 90:
        pitch = 90

    if pitch > 1:
        colColor = red
        PITCH = True

    colNr = round((pitch/22.5), 0)

    if TAIL:
        colNr = colStart-colNr
        if colNr == colStart:
            colNr -= 1
#            colColor = orange        # uncomment to visualize the resolution at small angles 
        TAIL = False
    else:
        colNr += colStart
        if colNr == colStart:
            colNr += 1
#            colColor = orange        # uncomment to visualize the resolution at small angles

    if roll >= 270:
        RIGHT = True
        roll = 360 - roll
        rowStart = 3
    else:
        rowStart = 4

    if roll > 90:
        roll = 90

    if roll > 1:
        rowColor = red
        ROLL = True

    rowNr = round((roll/22.5), 0)

    if RIGHT:
        rowNr += rowStart
        if rowNr == rowStart:
            rowNr += 1
#            rowColor = orange        # uncomment to visualize the resolution at small angles
        RIGHT = False
    else:
        rowNr = rowStart - rowNr
        if rowNr == rowStart:
            rowNr -= 1
#            rowColor = orange        # uncomment to visualize the resolution at small angles
                  
def drawLines():
    global  colDraw, colLast, colNr, PITCH, colColor, \
            rowDraw, rowLast, rowNr, ROLL,  rowColor, color

    if colLast != colNr:
        color = green
        colDraw = colLast
        drawCol()
        colLast = colNr

    if rowLast != rowNr:
        color = green
        rowDraw = rowLast
        drawRow()
        rowLast = rowNr

    color = colColor
    if PITCH:
        colDraw = colNr
        drawCol()
        
    color = rowColor
    if ROLL:
        rowDraw = rowNr
        drawRow()

    if PITCH and ROLL:
        sh.set_pixel(colNr,rowNr,blue)

    PITCH = False
    ROLL = False        

if __name__ == "__main__":

    setImuConfig()
    sh.clear(color)
    while True:
        getOrientation()
        calcLines()
        drawLines()
