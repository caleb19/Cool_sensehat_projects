#!/usr/bin/python
from sense_hat import SenseHat
import os,sys
import json
import urllib2
import datetime
import time
import pygame  
from pygame.locals import *
from uuid import getnode as get_mac
import IssFlags

pygame.init()
pygame.display.set_mode((640, 480))

sense = SenseHat()
flags = IssFlags

####
## Use of the API url's:
## url1 gets latitude and longitude of ISS'current position
## url2 gets countr(code) and timezone
## url3 gets latitude and longitude of current WIFI host's mac adress
## url4 gets formatted address of current RPi location
## url5 gets date and time of the next pass over the RPi location
####

url1 = 'https://api.wheretheiss.at/v1/satellites/25544'
url2 = 'https://api.wheretheiss.at/v1/coordinates/'

####
## url3 and url4 are Google api's and require a Google developers ApiKey
## ApiKey's are personal and therefor blanked out in this script
## One can obtain a free personal key at https://developers.google.com/maps/documentation/geocoding/intro
####

ApiKey1 = 'API_KEY'
ApiKey2 = 'API_KEY'

URL1_FOUND = False
URL3_FOUND = False
URL4_FOUND = False
URL5_FOUND = False

pixels = [
    [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
    [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
    [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
    [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
    [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
    [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
    [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
    [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
]

xList = [0,0,0,0,1,2,3,4,5,7,7,7,7,7,7,7,5,4,3,2,1,0,0,0,0]
yList = [3,4,5,7,7,7,7,7,7,7,5,4,3,2,1,0,0,0,0,0,0,0,1,2,3]

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (231, 255 , 7)
orange = (255,196,0)
color = black

msleep = lambda x: time.sleep(x / 1000.0)

sense.set_rotation(180)

PITCH    = False
colLast  = 0

ROLL     = False
rowLast  = 0

def solveMac():
    global ApiKey1,URL3_FOUND
    
    # Get and format mac address of the current wifi host
    mac = get_mac()
    MAC = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

    # Prepare request to Google for location of the mac address
    url3 = 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s' %(ApiKey1)
    data = {"wifiAccessPoints": [{"macAddress": MAC,},{"macAddress": MAC,},]}
    payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    req = urllib2.Request(url3)
    req.add_header('Content-Type', 'application/json')
    try:
        response = json.load(urllib2.urlopen(req, json.dumps(payload)))
    except urllib2.URLError as e:
        URL3_FOUND = False
        text = "mac not solved"
        sense.show_message(text,text_colour=white,back_colour=red)
    else:
        URL3_FOUND = True
        return response

def getHostLocation(response):
    global ApiKey2,URL4_FOUND

    #Prepare request to second Google API to convert coordinates 
    location = response['location']
    LAT = location['lat']
    LON = location['lng']
    #ACC = response['accuracy']
    url4 = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s' %(LAT,LON,ApiKey2)
    try:
        dict1 = json.load(urllib2.urlopen(url4))
    except urllib2.URLError as e:
        URL4_FOUND = False
        text = "address not solved"
        sense.show_message(text,text_colour=white,back_colour=red)
    else:
        URL4_FOUND = True
        return dict1, LAT, LON

def whereAmI():
    global URL3_FOUND,URL4_FOUND

    response = solveMac()
    if URL3_FOUND:
        dict1,LAT,LON = getHostLocation(response)
    if URL4_FOUND:
        # Prepare responses for display on lcd
        dict2 = dict1['results']
        dict3 = dict2[1]
        dict4 = dict3['formatted_address']
        CityStr = str(dict4)
        city = CityStr.split(",")
        City = str(city[0])
        Country = str(city[1])
        latStr, lngStr = displayCoordinates(LAT,LON)
        Location = '%s %s %s %s' % (City, Country,latStr,lngStr) 
        color = blue
        text(Location, color)
    return LAT, LON

def nextOverhead (LAT,LON):
    global URL5_FOUND
    
    LAT = str(LAT)
    LON = str(LON)
    url5 = 'http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' %(LAT,LON)
    try:
        response3 = json.load(urllib2.urlopen(url5))
    except urllib2.URLError as e:
        URL5_FOUND = False
        text = "No response of ESA api 3 !!" # nog displayen
    else:
        URL5_FOUND = True
        return response3

def getNextOverhead():
    global URL4_FOUND,URL5_FOUND
    
    LAT, LON = whereAmI()
    if URL4_FOUND:
        data1 = nextOverhead(LAT,LON)
    if URL5_FOUND:
        response1 = data1['response']
        dict5 = response1[0]
        riseTime = dict5['risetime']
        RiseTime = (datetime.datetime.fromtimestamp(int(riseTime)).strftime('%Y-%m-%d %H:%M:%S'))
        splitTimestamp = RiseTime.split(" ")
        splitDate=splitTimestamp[0].split("-")
        splitTime=splitTimestamp[1].split(":")
        RiseTime = splitDate[2] + "-" + splitDate[1] + " " + splitTime[0] + ":" + splitTime[1]
        duration = dict5['duration']
        overhead = 'ISS at %s for %s s' %(RiseTime,duration)
        color = yellow
        text(overhead, color)

def trackISS():
    global URL1_FOUND

    data1 = getLocationISS()
    if URL1_FOUND:
        data2 = processResponse(data1)
    time.sleep(10)
    sense.clear(black)

def getLocationISS():
    global URL1_FOUND

    try:
        response = json.load(urllib2.urlopen(url1))
    except urllib2.URLError as e:
        URL1_FOUND = False
        text = "No response of ESA"
        sense.show_message(text,text_colour=white,back_colour=red)
        sense.clear(black)
    else:
        URL1_FOUND = True
        return response

def processResponse(response):
    global url2

    latitude = response['latitude']
    longitude = response['longitude']

    # Construct URL for 2nd API call
    latitudeStr = str(latitude)
    longitudeStr = str(longitude)
    url3 = url2 + latitudeStr + ',' + longitudeStr     

    # Prepare coordinates for displaying
    latStr, lngStr = displayCoordinates(latitude,longitude)

    #Prepare display daylight/eclipsed
    light =  response['visibility']
    
    # Call 2nd API for enrichment (if above land)
    try:
        response2 = json.load(urllib2.urlopen(url3))
    except urllib2.HTTPError as e:
        text = str("Sea %s %s %s" % ( latStr, lngStr, light ))
        sense.show_message(text,text_colour=white,back_colour=blue)
        sense.clear(black)
    except urllib2.URLError as e:
        text = "No response of ESA"
        sense.show_message(text,text_colour=white,back_colour=red)
        sense.clear(black)
    else:
        countryCode = response2['country_code']
        string = response2['timezone_id']
        splitString = string.split("/")
        timeZone = splitString[1]
        flags.findFlag(countryCode,timeZone,light)

def displayCoordinates(latitude,longitude):
    latitude = round(latitude, 1)
    longitude = round(longitude, 1)
    if latitude <0:
        lat = " S"
    else:
        lat = " N"
    if longitude <0:
        lng = " W"
    else:
        lng = " E"
    latitude = abs(latitude)
    longitude = abs(longitude)
    latStr = str(latitude) + lat
    lngStr = str(longitude) + lng
    return latStr, lngStr    

def next_colour(pix):
    r = pix[0]
    g = pix[1]
    b = pix[2]

    if (r == 255 and g < 255 and b == 0):
        g += 1
    if (g == 255 and r > 0 and b == 0):
        r -= 1
    if (g == 255 and b < 255 and r == 0):
        b += 1
    if (b == 255 and g > 0 and r == 0):
        g -= 1
    if (b == 255 and r < 255 and g == 0):
        r += 1
    if (r == 255 and b > 0 and g == 0):
        b -= 1

    pix[0] = r
    pix[1] = g
    pix[2] = b

def rainbow():
    for pix in pixels:
        next_colour(pix)
        sense.set_pixels(pixels)
    msleep(1000)
    sense.clear(black)

def text(text, color):
    
    sense.show_message(text, text_colour=color)

def temperature(color):

    text("Tmp", color)
    temp = sense.temperature - 10
    sense.show_message("%d    " % temp, text_colour=color)
    sense.set_rotation(90)
    pixels = [red if i < temp else black for i in range(64)]
    sense.set_pixels(pixels)
    msleep(2000)
    sense.set_rotation(180)
    sense.clear(black)
    
def humidity(color):

    text("Hum", color)
    hum = sense.humidity
    humVal = 64 * hum / 100
    sense.show_message("%d   " % humVal, text_colour=color)
    sense.set_rotation(90)
    pixels = [blue if i < humVal else black for i in range(64)]
    sense.set_pixels(pixels)
    msleep(2000)
    sense.set_rotation(180)
    sense.clear(black)

def compass(color):

    text("Cmp", color)
    heading = sense.get_compass()                                     # disables gyro en accelerometer!
    sense.show_message("%d    " % heading, text_colour=color)
    index = int(heading / 15+1)
    x = xList[index]
    y = yList[index]    
    sense.set_pixel(x, y, color)
    msleep(2000)
    sense.clear(black)
    
def pressure(color):
      
    text("Bar", color)
    press = sense.get_pressure()
    sense.show_message("%d    " % press, text_colour=color)

def computeHeight(pressure):
    return 44330.8 * (1 - pow(pressure / 1013.25, 0.190263));
    
def height(color):

    text("Sea", color)
    pressure = sense.get_pressure()
    height = computeHeight(pressure)
    sense.show_message("%d    " % height, text_colour=color)

def setImuConfig():
    sense.set_imu_config(True, True, True)
    
def getOrientation():
      
    levels = {}

    levels = sense.get_orientation_degrees()
    pitch = int(levels['pitch'])
    roll = int(levels['roll'])
    yaw = int(levels['yaw'])
	
    return pitch, roll, yaw
    
def angles(color):
      
    setImuConfig()
    pitch, roll, yaw = getOrientation()
    text("Pitch", color)
    sense.show_message("%d    " % pitch, text_colour=color)
    text("Roll", color)
    sense.show_message("%d    " % roll, text_colour=color)

def calcLines(pitch, roll):
    
    global PITCH, ROLL

    TAIL  = False
    RIGHT = False
	
    if pitch >= 270:
        TAIL = True
        pitch = 360 - pitch
        colStart = 4
    else:
        colStart = 3

    if pitch > 90:
        pitch = 90

    if pitch > 1:
        PITCH = True

    colNr = round((pitch/22.5), 0)

    if TAIL:
        colNr = colStart-colNr
        if colNr == colStart:
            colNr -= 1
        TAIL = False
    else:
        colNr += colStart
        if colNr == colStart:
            colNr += 1

    if roll >= 270:
        RIGHT = True
        roll = 360 - roll
        rowStart = 3
    else:
        rowStart = 4

    if roll > 90:
        roll = 90

    if roll > 1:
        ROLL = True

    rowNr = round((roll/22.5), 0)

    if RIGHT:
        rowNr += rowStart
        if rowNr == rowStart:
            rowNr += 1
        RIGHT = False
    else:
        rowNr = rowStart - rowNr
        if rowNr == rowStart:
            rowNr -= 1
			
    return colNr, rowNr

def drawLines(colNr, rowNr):
    
    global  colLast, PITCH, rowLast, ROLL

    if colLast != colNr:
        drawCol(black, colLast)
        colLast = colNr

    if rowLast != rowNr:
        drawRow(black, rowLast)
        rowLast = rowNr

    if PITCH:
        drawCol(red, colNr)

    if ROLL:
        drawRow(red, rowNr)

    if PITCH or ROLL:
        drawRow(red, rowNr)
        drawCol(red, colNr)

    if PITCH and ROLL:
        sense.set_pixel(colNr,rowNr,blue)

    PITCH = False
    ROLL = False        

def drawCol(color, colNr):
    
    y = 0
    while (y <= 7):
        sense.set_pixel(colNr,y,color)
        y +=1

def drawRow(color, rowNr):
    
    x = 0
    while (x <= 7):
        sense.set_pixel(x,rowNr,color)
        x +=1

def showLevels():
    
    setImuConfig()
    sense.clear(black)
    IDLE = False
    idleTime = 0
    while idleTime < 10:
        pitch, roll, yaw = getOrientation()
        if pitch >= 355 or pitch <= 5:
            if roll >= 355 or roll <= 5:
                if IDLE:
                    currentTime = time.time()
                    idleTime = currentTime - startIdleTime
                else:
                    IDLE = True
                    startIdleTime = time.time()
            else:
                IDLE = False
        else:
            IDLE = False
        colNr, rowNr = calcLines(pitch, roll)
        drawLines(colNr, rowNr)
    rainbow()
    sense.clear(black)
    
def environmentals():
    temperature(red)
    humidity(blue)
    pressure(yellow)
    height(green)
    compass(white)
    angles(orange)
    rainbow()
    sense.clear(black)
    
def endScript(color):
    text("Shutdown ..... ", color)
    sense.clear(black)
    pygame.quit()
    sys.exit(0)

#Listen for joystick events
def handle_event(event):
    if event.type == KEYDOWN:
        if event.key == pygame.K_DOWN:
            environmentals()
        elif event.key == pygame.K_UP:
            showLevels()
        elif event.key == pygame.K_LEFT:
            getNextOverhead()
        elif event.key == pygame.K_RIGHT:
            rainbow()
        elif event.key == pygame.K_RETURN:
            endScript(red)
    pygame.event.clear()
    
text("RPi", white)
text("SH", red)
text("RPi", blue)
text("SH", green)

rainbow()

if __name__ == "__main__":
    while True:
        try: 
            for event in pygame.event.get():
                handle_event(event)
            trackISS()
        except (KeyboardInterrupt):
            sense.clear()
            sys.exit(0)
