#!/usr/bin/python
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)

red       = [255,  0,  0]
blue      = [  0,  0,255]
green     = [  0,255,  0]
black     = [  0,  0,  0]
white     = [255,255,255]
yellow    = [255,255,  0]
orange    = [255,196,  0]
turquoise = [100,225,221]
skyblue   = [  0,176,240]
softgreen = [  0,176, 80]
darkgreen = [131, 84, 40]  
purple    = [255,  0,255]

def findFlag(countryCode,timeZone,daylight):

    print countryCode, timeZone # For debugging

    if countryCode == "??":
        text = str("No-man's-land %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        S = skyblue
        R = red
        G = softgreen

        nomansland = [
        S,S,S,R,R,S,S,S,
        S,S,R,S,S,R,S,S,
        S,S,S,S,S,R,S,S,
        S,S,S,S,R,S,S,S,
        S,S,S,R,S,S,S,S,
        G,G,G,R,G,G,G,G,
        G,G,G,G,G,G,G,G,
        G,G,G,R,G,G,G,G]
        sense.set_pixels(nomansland)

    elif countryCode == "AD":
        text = str("Andorra %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = yellow 
        b = blue
                
        Andorra  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,X,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Andorra)
    
    elif countryCode == "AE":
        text = str("Emirates %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white
        O = green
        Z = blue
        R = red

        Emirates = [
        R,R,O,O,O,O,O,O,
        R,R,O,O,O,O,O,O,
        R,R,O,O,O,O,O,O,
        R,R,X,X,X,X,X,X,
        R,R,X,X,X,X,X,X,
        R,R,Z,Z,Z,Z,Z,Z,
        R,R,Z,Z,Z,Z,Z,Z,
        R,R,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Emirates)

    elif countryCode == "AF":
        text = str("Afghanistan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        F = black
        B = red
        S = white
                
        Afhanistan = [
        F,F,F,B,B,X,X,X,
        F,F,F,B,B,X,X,X,
        F,F,F,S,S,X,X,X,
        F,F,S,S,S,S,X,X,
        F,F,S,S,S,S,X,X,
        F,F,F,S,S,X,X,X,
        F,F,F,B,B,X,X,X,
        F,F,F,B,B,X,X,X]
        sense.set_pixels(Afhanistan)
                
    elif countryCode == "AG":
        text = str("Barbuda %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        R = red
        Z = black
        B = blue
        W = white
        Y = yellow
                
        Barbuda = [
        Z,Z,Z,Z,Z,Z,Z,Z,
        R,Z,Z,Y,Y,Z,Z,R,
        R,R,Z,Y,Y,Z,R,R,
        R,R,B,B,B,B,R,R,
        R,R,B,B,B,B,R,R,
        R,R,W,W,W,W,R,R,
        R,R,R,W,W,R,R,R,
        R,R,R,R,R,R,R,R]
        sense.set_pixels(Barbuda)
    
    elif countryCode == "AI":
        text = str("Anguila %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        W = white
        R = red
        Y = yellow

        Anguila = [ 
        W,R,W,X,X,X,X,X,
        R,R,R,X,X,X,X,X,
        W,R,W,X,X,X,X,X,
        X,X,X,X,W,W,W,X,
        X,X,X,X,W,Y,W,X,
        X,X,X,X,X,W,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Anguila)

    elif countryCode == "AL":
        text = str("Albania %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        O = red
        B = black

        Albania = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,B,O,O,B,O,O,
        O,O,B,B,B,B,O,O,
        O,O,B,B,B,B,O,O,
        O,O,B,O,O,B,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Albania)


    elif countryCode == "AM":
        text = str("Armenia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        O = red
        Z = orange

        Armenia = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Armenia)

    elif countryCode == "AO":
        text = str("Angola %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = yellow  
        T = black 

        Angola = [  
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,O,O,X,X,X,
        T,T,T,O,O,T,T,T,
        T,T,T,T,T,T,T,T,
        T,T,T,T,T,T,T,T,
        T,T,T,T,T,T,T,T]
        sense.set_pixels(Angola)

    elif countryCode == "AQ":
        text = str("Antartica %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        O = blue
        B = white

        Antartica = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,B,B,O,O,
        O,O,B,B,B,B,O,O,
        O,O,B,B,B,B,O,O,
        O,O,B,B,O,B,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Antartica)

    elif countryCode == "AR":
        text = str("Argentina %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = turquoise 
        O = white 
        Y = orange
                
        Argentina = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,Y,Y,O,O,O,
        O,O,O,Y,Y,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Argentina)

    elif countryCode == "AS":
        text = str("Samoa %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        B = blue
        W = white
        R = red
        Y = yellow

        Samoa = [ 
        B,B,B,B,B,B,R,R,
        B,B,B,B,R,R,W,W,
        B,R,R,R,W,W,W,W,
        B,R,W,W,W,W,R,W,
        B,R,W,W,W,W,R,W,
        B,R,R,R,W,W,Y,W,
        B,B,B,B,R,R,W,W,
        B,B,B,B,B,B,R,R]
        sense.set_pixels(Samoa)

    elif countryCode == "AT":
        text = str("Austria %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)
    
        X = red
        O = white

        Austria = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Austria)

    elif countryCode == "AU":
        text = str("Australia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        W = white
        R = red

        Australia = [ 
        W,R,W,X,X,X,X,X,
        R,R,R,X,X,W,X,X,
        W,R,W,X,X,X,X,X,
        X,X,X,X,X,X,W,X,
        X,X,X,X,X,X,X,X,
        X,W,W,X,X,X,X,X,
        X,W,W,X,X,W,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Australia)

    elif countryCode == "AW":
        text = str("Aruba %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        W = white
        R = red
        Y = yellow

        Aruba = [ 
        X,X,X,X,X,X,X,X,
        X,X,R,X,X,X,X,X,
        X,R,R,R,X,X,X,X,
        X,X,R,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        Y,Y,Y,Y,Y,Y,Y,Y,
        Y,Y,Y,Y,Y,Y,Y,Y,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Aruba)

    elif countryCode == "AX":
        text = str("Aland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        W = white
        R = red

        Aland = [ 
        X,X,W,R,W,X,X,X,
        X,X,W,R,W,X,X,X,
        X,X,W,R,W,X,X,X,
        W,W,W,R,W,W,W,W,
        R,R,R,R,R,R,R,R,
        W,W,W,R,W,W,W,W,
        X,X,W,R,W,X,X,X,
        X,X,W,R,W,X,X,X]
        sense.set_pixels(Aland)


    elif countryCode == "AZ":
        text = str("Azerbaijan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = blue
        Z = green
        W = white

        Azerbaijan = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,W,W,X,X,X,
        X,X,X,W,W,X,X,X,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Azerbaijan)

    elif countryCode == "BA":
        text = str("Bosnia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue 
        y = yellow 
        w = white
                
        Bosnia  = [ 
        b,b,w,y,y,y,y,b,
        b,b,w,y,y,y,y,b,
        b,b,b,w,y,y,y,b,
        b,b,b,w,y,y,y,b,
        b,b,b,b,w,y,y,b,
        b,b,b,b,w,y,y,b,
        b,b,b,b,b,w,y,b,
        b,b,b,b,b,w,y,b]
        sense.set_pixels(Bosnia)


    elif countryCode == "BB":
        text = str("Barbados %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        O = yellow 
        b =  blue
        z = black
                
        Barbados  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,z,O,X,X,
        b,b,b,O,z,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Barbados)

    elif countryCode == "BD":
        text = str("Bangladesh %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = green

        Bangladesh = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,X,X,X,O,O,O,
        O,O,X,X,X,O,O,O,
        O,O,X,X,X,O,O,O,
        O,O,X,X,X,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Bangladesh)

    elif countryCode == "BE":
        text = str("Belgium %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = yellow 
        b = black
                
        Belgium  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Belgium)

    elif countryCode == "BF":
        text = str("Burkina Faso %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red 
        y = yellow 
        g = green
                
        Burkina  = [ 
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,y,y,r,r,r,
        g,g,g,y,y,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g]
        sense.set_pixels(Burkina)

        
    elif countryCode == "BG":
        text = str("Bulgaria %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        O = white
        Z = red

        Bulgaria = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Bulgaria)

    elif countryCode == "BH":
        text = str("Bahrain %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b=  white
        X = red
                
        Bahrain  = [ 
        b,b,X,X,X,X,X,X,
        b,b,b,X,X,X,X,X,
        b,b,X,X,X,X,X,X,
        b,b,b,X,X,X,X,X,
        b,b,X,X,X,X,X,X,
        b,b,b,X,X,X,X,X,
        b,b,X,X,X,X,X,X,
        b,b,b,X,X,X,X,X]
        sense.set_pixels(Bahrain)

    elif countryCode == "BI":
        text = str("Burundi %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        w = white
        r = red
        g = green
        
        Burundi = [
        w,r,r,r,r,r,r,w,
        g,w,r,r,r,r,w,g,
        g,g,w,r,r,w,g,g,
        g,g,g,w,w,g,g,g,
        g,g,g,w,w,g,g,g,
        g,g,w,r,r,w,g,g,
        g,w,r,r,r,r,w,g,
        w,r,r,r,r,r,r,w]
        sense.set_pixels(Burundi)

    elif countryCode == "BJ":
        text = str("Benin %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        y = yellow
        r = red
        g = green
        
        Benin = [
        g,g,g,y,y,y,y,y,
        g,g,g,y,y,y,y,y,
        g,g,g,y,y,y,y,y,
        g,g,g,y,y,y,y,y,
        g,g,g,r,r,r,r,r,
        g,g,g,r,r,r,r,r,
        g,g,g,r,r,r,r,r,
        g,g,g,r,r,r,r,r]
        sense.set_pixels(Benin)

    elif countryCode == "BL":
        text = str("St Barthelemy %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)
        
        X = red 
        O = white 
        b=  blue
                
        StBarthelemy  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(StBarthelemy)
        
    elif countryCode == "BM":
        text = str("Bermuda %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        W = white
        R = red

        Bermuda = [ 
        X,W,R,W,X,R,R,R,
        R,R,R,R,R,R,R,R,
        X,W,R,W,X,R,W,R,
        R,R,R,R,R,R,W,R,
        R,R,R,R,R,R,W,R,
        R,R,R,R,R,R,W,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R]
        sense.set_pixels(Bermuda)

    elif countryCode == "BN":
        text = str("Brunei %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        y = yellow
        r = red
        w = white
        z = black

        Brunei = [
        y,y,y,y,y,y,y,y,
        w,w,y,y,y,y,y,y,
        z,z,w,w,y,y,y,y,
        y,y,z,r,r,w,y,y,
        y,y,y,r,r,z,w,w,
        y,y,y,y,y,y,z,z,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y]
        sense.set_pixels(Brunei)

    elif countryCode == "BO":
        text = str("Bolivia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = yellow 
        M = green

        Bolivia = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        M,M,M,M,M,M,M,M,
        M,M,M,M,M,M,M,M,
        M,M,M,M,M,M,M,M]
        sense.set_pixels(Bolivia)

    elif countryCode == "BQ":
        text = str("Bonaire %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = white 
        M = blue

        Bonaire = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        M,M,M,M,M,M,M,M,
        M,M,M,M,M,M,M,M,
        M,M,M,M,M,M,M,M]
        sense.set_pixels(Bonaire)

    elif countryCode == "BR":
        text = str("Brazil %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        O = blue
        Z = yellow

        Brazil = [
        X,X,X,Z,Z,X,X,X,
        X,X,Z,O,O,Z,X,X,
        X,Z,O,O,O,O,Z,X,
        Z,O,O,O,O,O,O,Z,
        Z,O,O,O,O,O,O,Z,
        X,Z,O,O,O,O,Z,X,
        X,X,Z,O,O,Z,X,X,
        X,X,X,Z,Z,X,X,X,
        ]
        sense.set_pixels(Brazil)

    elif countryCode == "BS":
        text = str("Bahamas %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = skyblue  
        O = yellow 
        M = skyblue
        B = blue

        Bahamas = [ 
        X,X,X,X,X,X,X,X,
        B,X,X,X,X,X,X,X,
        B,B,X,X,X,X,X,X,
        B,B,B,O,O,O,O,O,
        B,B,B,O,O,O,O,O,
        B,B,M,M,M,M,M,M,
        B,M,M,M,M,M,M,M,
        M,M,M,M,M,M,M,M]
        sense.set_pixels(Bahamas)

    elif countryCode == "BT":
        text = str("Bhutan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = yellow 
        O = red 
        M = white

        Bhutan = [ 
        X,X,X,X,X,X,X,O,
        X,X,X,X,X,X,O,O,
        X,X,X,X,M,M,O,O,
        X,X,X,M,M,O,O,O,
        X,X,M,M,O,M,O,O,
        X,X,M,O,M,O,O,O,
        X,X,M,O,O,O,O,O,
        X,O,O,O,O,O,O,O]
        sense.set_pixels(Bhutan)

    elif countryCode == "BT":
        text = str("Bouvet Island %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        W = white
        R = blue

        BouvetIsland = [ 
        X,X,W,R,W,X,X,X,
        X,X,W,R,W,X,X,X,
        X,X,W,R,W,X,X,X,
        W,W,W,R,W,W,W,W,
        R,R,R,R,R,R,R,R,
        W,W,W,R,W,X,X,X,
        X,X,W,R,W,X,X,X,
        X,X,W,R,W,X,X,X]
        sense.set_pixels(BouvetIsland)

    elif countryCode == "BW":
        text = str("Botswana %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = skyblue  
        O = blue 
        M = skyblue

        Botswana = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        M,M,M,M,M,M,M,M,
        M,M,M,M,M,M,M,M,
        M,M,M,M,M,M,M,M]
        sense.set_pixels(Botswana)

    elif countryCode == "BY":
        text = str("Belarus %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = white 
        M = green

        Belarus = [ 
        X,O,X,X,X,X,X,X,
        O,X,X,X,X,X,X,X,
        X,O,X,X,X,X,X,X,
        O,X,X,X,X,X,X,X,
        X,O,X,X,X,X,X,X,
        O,X,X,X,X,X,X,X,
        X,O,M,M,M,M,M,M,
        O,X,M,M,M,M,M,M]
        sense.set_pixels(Belarus)
        
    elif countryCode == "BZ":
        text = str("Belize %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue  
        O = white 
        M = red
        G = green

        Belize = [ 
        M,M,M,M,M,M,M,M,
        X,X,X,X,X,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,O,O,G,O,X,X,
        X,X,O,G,O,O,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,X,X,X,X,X,
        M,M,M,M,M,M,M,M]
        sense.set_pixels(Belize)

    elif countryCode == "CA":
        text = str("Canada %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
             
        Canada = [ 
        X,O,O,O,O,O,O,X,
        X,O,O,O,O,O,O,X,
        X,O,O,X,X,O,O,X,
        X,O,X,X,X,X,O,X,
        X,O,X,X,X,X,O,X,
        X,O,O,O,O,O,O,X,
        X,O,O,O,O,O,O,X,
        X,O,O,O,O,O,O,X] 
        sense.set_pixels(Canada)

    elif countryCode == "CC":
        text = str("Keeling Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        G = green 
        Y = yellow 
        
        Keeling = [ 
        G,G,G,G,G,G,G,G,
        G,Y,Y,G,G,G,Y,G,
        G,Y,Y,G,G,G,G,G,
        G,G,G,G,Y,G,Y,G,
        G,G,G,Y,G,G,G,G,
        G,G,G,G,Y,G,Y,G,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G] 
        sense.set_pixels(Keeling)

    elif countryCode == "CD":
        text = str("Congo %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue  
        O = yellow 
        T = red

        Congo = [
        X,X,X,X,X,X,T,T,
        X,O,X,X,X,T,T,X,
        X,X,X,X,T,T,X,X,
        X,X,X,T,T,X,X,X,
        X,X,T,T,X,X,X,X,
        X,T,T,X,X,X,X,X,
        T,T,X,X,X,X,X,X,
        T,X,X,X,X,X,X,X] 
        sense.set_pixels(Congo)

    elif countryCode == "CF":
        text = str("Central African Republic %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue  
        O = white 
        M = green
        A = red
        Y = yellow
        Z = black

        CntrAfrica = [ 
        X,X,X,A,A,X,X,X,
        X,Y,X,A,A,X,X,X,
        O,O,O,A,A,O,O,O,
        O,O,O,A,A,O,O,O,
        M,M,M,A,A,M,M,M,
        M,M,M,A,A,M,M,M,
        Z,Z,Z,A,A,Z,Z,Z,
        Z,Z,Z,A,A,Z,Z,Z]
        sense.set_pixels(CntrAfrica)
        
    elif countryCode == "CH":
        text = str("Switzerland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = white
                
        Switzerland = [ 
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X] 
        sense.set_pixels(Switzerland)

    elif countryCode == "CI":
        text = str("Cote d Ivoir %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        O = white 
        b = orange
                
        CotedIvoir  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(CotedIvoir)

    elif countryCode == "CK":
        text = str("Cook Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        W = white
        R = red

        Cook = [ 
        W,R,W,X,X,X,X,X,
        R,R,R,X,X,X,X,X,
        W,R,W,X,W,W,X,X,
        X,X,X,W,X,X,W,X,
        X,X,X,W,X,X,W,X,
        X,X,X,X,W,W,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Cook)

    elif countryCode == "CL":
        text = str("Chile %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white  
        R = red
        B = blue
                
        Chile = [ 
        B,B,B,B,X,X,X,X,
        B,X,X,B,X,X,X,X,
        B,X,X,B,X,X,X,X,
        B,B,B,B,X,X,X,X,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,] 
        sense.set_pixels(Chile)

    elif countryCode == "CM":
        text = str("Cameroon %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = yellow 
        O = red 
        b = green
                
        Cameroon  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,X,O,X,X,
        b,b,b,O,X,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Cameroon)

    elif countryCode == "CN":
        text = str("China %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = yellow 
                
        China = [ 
        X,X,X,O,X,X,X,X,
        X,O,O,X,O,X,X,X,
        X,O,O,X,O,X,X,X,
        X,X,X,O,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X
        ] 
        sense.set_pixels(China)

    elif countryCode == "CO":
        text = str("Colombia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        O = yellow
        Z = red

        Colombia = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Colombia)

    elif countryCode == "CR":
        text = str("Costa Rica %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white
        O = blue
        R = red

        CostaRica = [
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        R,R,R,R,R,R,R,R,
        R,R,R,X,X,R,R,R,
        R,R,R,X,X,R,R,R,
        R,R,R,R,R,R,R,R,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(CostaRica)

    elif countryCode == "CU":
        text = str("Cuba %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue
        O = white
        R = red

        Cuba = [
        R,O,O,O,O,O,O,O,
        R,R,X,X,X,X,X,X,
        R,X,R,O,O,O,O,O,
        R,X,X,R,X,X,X,X,
        R,X,R,R,O,O,O,O,
        R,R,R,X,X,X,X,X,
        R,R,O,O,O,O,O,O,
        R,O,O,O,O,O,O,O]
        sense.set_pixels(Cuba)

    elif countryCode == "CV":
        text = str("Cabo Verde %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white
        O = blue
        Z = red
        Y = yellow

        CaboVerde = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,Y,Y,O,O,O,O,
        X,Y,X,X,Y,X,X,X,
        Z,Y,Z,Z,Y,Z,Z,Z,        
        X,Y,X,X,Y,X,X,X,
        O,O,Y,Y,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(CaboVerde)

    elif countryCode == "CW":
        text = str("Curacao %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        W = white
        O = blue
        X = yellow

        Curacao = [
        O,O,O,O,O,O,O,O,
        O,W,O,O,O,O,O,O,
        O,O,O,W,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,        
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Curacao)
        
    elif countryCode == "CX":
        text = str("Christmas Island %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        b = blue
        y = yellow
        w = white
        
        XmasIsland = [
        g,g,g,g,g,g,g,g,
        b,g,g,g,g,y,y,g,
        b,b,g,g,g,g,g,g,
        b,b,b,y,y,g,g,g,
        b,w,b,y,y,g,g,g,
        b,b,b,b,b,b,g,g,
        b,w,b,w,b,b,b,g,
        b,b,b,b,b,b,b,b]
        sense.set_pixels(XmasIsland)

    elif countryCode == "CY":
        text = str("Cyprus %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        O = orange
        W = white
        G = green

        Cyprus = [ 
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,O,W,
        W,W,O,W,W,O,O,W,
        W,W,O,O,O,O,W,W,
        W,W,W,O,W,W,W,W,
        W,G,W,W,W,G,W,W,
        W,W,G,G,G,W,W,W,
        W,W,W,W,W,W,W,W]
        sense.set_pixels(Cyprus)

    elif countryCode == "CZ":
        text = str("Czech Republic %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = white
        R = blue

        Czechia = [
        R,O,O,O,O,O,O,O,
        R,R,O,O,O,O,O,O,
        R,R,R,O,O,O,O,O,
        R,R,R,R,O,O,O,O,
        R,R,R,R,X,X,X,X,
        R,R,R,X,X,X,X,X,
        R,R,X,X,X,X,X,X,
        R,O,X,X,X,X,X,X]
        sense.set_pixels(Czechia)

    elif countryCode == "DE":
        text = str("Germany %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)
    
        X = red
        O = black
        Z = yellow

        Germany = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Germany)
        
    elif countryCode == "DJ":
        text = str("Djibouti %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        g = green
        w = white
        r = red

        Djibouti = [
        w,b,b,b,b,b,b,b,
        w,w,b,b,b,b,b,b,
        w,w,w,b,b,b,b,b,
        w,r,r,w,b,b,b,b,
        w,r,r,w,g,g,g,g,
        w,w,w,g,g,g,g,g,
        w,w,g,g,g,g,g,g,
        w,g,g,g,g,g,g,g]
        sense.set_pixels(Djibouti)

    elif countryCode == "DK":
        text = str("Denmark %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white
        O = red
        T = black

        Denmark = [ 
        O,O,X,X,O,O,O,O,
        O,O,X,X,O,O,O,O,
        O,O,X,X,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,X,X,O,O,O,O,
        O,O,X,X,O,O,O,O,
        O,O,X,X,O,O,O,O] 
        sense.set_pixels(Denmark)

    elif countryCode == "DM":
        text = str("Dominica %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        y = yellow
        b = black
        w = white
        r = red
        p = purple

        Dominica = [
        g,g,g,y,b,w,g,g,
        g,g,g,y,b,w,g,g,
        g,g,g,r,r,w,g,g,
        y,y,r,p,g,r,y,y,
        b,b,r,p,g,r,b,b,
        w,w,w,r,r,w,w,w,
        g,g,g,y,b,w,g,g,
        g,g,g,y,b,w,g,g]
        sense.set_pixels(Dominica)

    elif countryCode == "DO":
        text = str("Dominican Republic %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white
        O = red
        B = blue

        DominicanR = [ 
        B,B,B,X,X,O,O,O,
        B,B,B,X,X,O,O,O,
        B,B,B,X,X,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,X,X,B,B,B,
        O,O,O,X,X,B,B,B,
        O,O,O,X,X,B,B,B] 
        sense.set_pixels(DominicanR)

    elif countryCode == "DZ":
        text = str("Algeria %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        T = green
        
        Algeria = [ 
        T,T,T,T,O,O,O,O,
        T,T,T,T,O,O,O,O,
        T,T,T,T,O,O,O,O, 
        T,T,T,X,X,O,O,O,
        T,T,T,X,X,O,O,O,
        T,T,T,T,O,O,O,O,
        T,T,T,T,O,O,O,O,
        T,T,T,T,O,O,O,O] 
        sense.set_pixels(Algeria) 

    elif countryCode == "EC":
        text = str("Ecuador %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = yellow 
        T = blue
        Z = black
        G = green
        Y = yellow
        
        Ecuador = [ 
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,Z,Z,O,O,O, 
        T,T,T,G,G,T,T,T,
        T,T,T,Y,Y,T,T,T,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X] 
        sense.set_pixels(Ecuador) 

    elif countryCode == "EE":
        text = str("Estonia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white 
        O = blue 
        T = black
        
        Estonia = [ 
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O, 
        T,T,T,T,T,T,T,T,
        T,T,T,T,T,T,T,T,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X] 
        sense.set_pixels(Estonia) 

    elif countryCode == "EG":
        text = str("Egypt %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = black
        O = red
        Z = yellow
        W = white
        
        Egypt = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        W,W,W,W,W,W,W,W,
        W,W,W,Z,Z,W,W,W,
        W,W,W,Z,Z,W,W,W,
        W,W,W,W,W,W,W,W,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Egypt)

    elif countryCode == "EH":
        text = str("Western Sahara %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        W = white
        O = blue
        R = red

        Sahara = [
        R,O,O,O,O,O,O,O,
        R,R,O,O,O,O,O,O,
        R,R,R,O,O,O,O,O,
        R,R,R,R,W,W,W,W,
        R,R,R,R,W,R,W,W,
        R,R,R,W,W,W,W,W,
        R,R,X,X,X,X,X,X,
        R,O,X,X,X,X,X,X]
        sense.set_pixels(Sahara)
       
    elif countryCode == "ER":
        text = str("Eritrea %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        r = red
        b = blue
        y = yellow

        Eritrea = [
        r,r,g,g,g,g,g,g,
        r,r,r,r,g,g,g,g,
        r,r,r,r,r,r,g,g,
        r,y,y,r,r,r,r,r,
        r,y,y,r,r,r,r,r,
        r,r,r,r,r,r,b,b,
        r,r,r,r,b,b,b,b,
        r,r,b,b,b,b,b,b]
        sense.set_pixels(Eritrea)

    elif countryCode == "ES":
        text = str("Spain %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)
        
        O = yellow
        X = red
        B = black

        Spain = [
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,B,B,O,O,O,
        O,O,O,B,B,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Spain)

    elif countryCode == "ET":
        text = str("Ethiopia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        O = red
        Z = yellow
        S = blue

        Ethiopia = [
        X,X,X,X,X,X,X,X,
        X,X,X,S,S,X,X,X,
        X,X,X,S,S,X,X,X,
        Z,Z,S,Z,Z,S,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Ethiopia)

    elif countryCode == "FI":
        text = str("Finland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        w = white
        b = blue

        Finland = [
        w,w,b,b,w,w,w,w,
        w,w,b,b,w,w,w,w,
        w,w,b,b,w,w,w,w,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        w,w,b,b,w,w,w,w,
        w,w,b,b,w,w,w,w,
        w,w,b,b,w,w,w,w]
        sense.set_pixels(Finland)

    elif countryCode == "FJ":
        text = str("Fiji %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        r = red
        w = white
        s = skyblue

        Fiji = [
        b,w,r,w,b,s,s,s,
        w,r,r,r,w,s,s,s,
        b,w,r,w,b,s,s,s,
        s,s,s,s,s,s,s,s,
        s,s,s,s,s,s,r,s,
        s,s,s,s,s,r,r,r,
        s,s,s,s,s,s,r,s,
        s,s,s,s,s,s,s,s]
        sense.set_pixels(Fiji)
  
    elif countryCode == "FK":
        text = str("Falklands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        r = red
        w = white
        s = skyblue
        y = yellow

        Falklands = [
        b,w,r,w,b,b,b,b,
        w,r,r,r,w,b,b,b,
        b,w,r,w,b,b,b,b,
        b,b,b,b,s,s,s,b,
        b,b,b,b,s,w,s,b,
        b,b,b,b,s,y,s,b,
        b,b,b,b,b,s,b,b,
        b,b,b,b,b,b,b,b]
        sense.set_pixels(Falklands)        

    elif countryCode == "FM":
        text = str("Micronesia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        s = skyblue
        w = white

        Micronesia = [
        s,s,s,s,s,s,s,s,
        s,s,s,w,w,s,s,s,
        s,s,s,s,s,s,s,s,
        s,w,s,s,s,s,w,s,
        s,w,s,s,s,s,w,s,
        s,s,s,s,s,s,s,s,
        s,s,s,w,w,s,s,s,
        s,s,s,s,s,s,s,s]
        sense.set_pixels(Micronesia)

    elif countryCode == "FO":
        text = str("Faroer Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        w = white
        b = blue
        r = red

        Faroer = [
        w,w,b,r,b,w,w,w,
        w,w,b,r,b,w,w,w,
        b,b,b,r,b,b,b,b,
        r,r,r,r,r,r,r,r,
        b,b,b,r,b,b,b,b,
        w,w,b,r,b,w,w,w,
        w,w,b,r,b,w,w,w,
        w,w,b,r,b,w,w,w]
        sense.set_pixels(Faroer)

    elif countryCode == "FR":
        text = str("France %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)
        
        X = red 
        O = white 
        b=  blue
                
        France  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(France)

    elif countryCode == "GA":
        text = str("Gabon %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = yellow
        O = green
        Z = blue

        Gabon = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Gabon)

    if countryCode == "GB":
        text = str("Great Brittain %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)
  
        X = red
        O = white
        B = blue

        GB = [
        B,B,O,X,X,O,B,B,
        B,B,O,X,X,O,B,B,
        O,O,O,X,X,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,X,X,O,O,O,
        B,B,O,X,X,O,B,B,
        B,B,O,X,X,O,B,B]
        sense.set_pixels(GB)

    elif countryCode == "GD":
        text = str("Grenada %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        y = yellow
        g = green

        Grenada = [
        r,r,r,r,r,r,r,r,
        r,y,y,y,y,y,y,r,
        r,g,y,y,y,y,g,r,
        r,g,g,r,y,g,g,r,
        r,g,g,y,r,g,g,r,
        r,g,y,y,y,y,g,r,
        r,y,y,y,y,y,y,r,
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Grenada)
        
    elif countryCode == "GE":
        text = str("Georgia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = white

        Georgia = [
        O,O,O,X,X,O,O,O,
        O,X,O,X,X,O,X,O,
        O,O,O,X,X,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,X,X,O,O,O,
        O,X,O,X,X,O,X,O,
        O,O,O,X,X,O,O,O]
        sense.set_pixels(Georgia)

    elif countryCode == "GF":
        text = str("French Guiana %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        b=  blue
                
        FrGuiana  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(FrGuiana)

    elif countryCode == "GG":
        text = str("Guernsey %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        w = white
        r = red
        y = yellow

        Guernsey = [
        w,w,r,r,r,w,w,w,
        w,w,r,y,r,w,w,w,
        w,w,r,y,r,w,w,w,
        r,r,r,y,r,r,r,r,
        r,y,y,y,y,y,r,r,
        r,r,r,y,r,r,r,r,
        w,w,r,y,r,w,w,w,
        w,w,r,r,r,w,w,w]
        sense.set_pixels(Guernsey)

    elif countryCode == "GH":
        text = str("Ghana %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        y = yellow
        g = green
        b = black

        Ghana = [
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        y,y,y,y,b,y,y,y,
        y,y,b,b,b,b,b,y,
        y,y,y,b,y,b,y,y,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g]
        sense.set_pixels(Ghana)
        
    elif countryCode == "GI":
        text = str("Gibraltar %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        w = white
        r = red
        y = yellow

        Gibraltar = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,r,r,r,w,w,
        w,w,w,r,y,r,w,w,
        w,w,w,r,y,r,w,w,
        r,r,r,r,y,r,r,r,      
        r,r,r,y,y,r,r,r,      
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Gibraltar)

    elif countryCode == "GL":
        text = str("Greenland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        R = red 
        W = white 
                
        Greenland  = [ 
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,R,W,W,W,W,W,
        W,R,R,R,W,W,W,W,
        R,W,W,W,R,R,R,R,
        R,R,W,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R]
        sense.set_pixels(Greenland)
        
    elif countryCode == "GM":
        text = str("Gambia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        w = white
        b = blue
        g = green

        Gambia = [
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        w,w,w,w,w,w,w,w,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        w,w,w,w,w,w,w,w,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g]
        sense.set_pixels(Gambia)

    elif countryCode == "GN":
        text = str("Guinea %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        F = green
        G = yellow

        Guinea = [
        X,X,X,G,G,G,F,F, 
        X,X,X,G,G,G,F,F,
        X,X,X,G,G,G,F,F, 
        X,X,X,G,G,G,F,F,
        X,X,X,G,G,G,F,F,
        X,X,X,G,G,G,F,F,
        X,X,X,G,G,G,F,F, 
        X,X,X,G,G,G,F,F
        ]
        sense.set_pixels(Guinea)

    elif countryCode == "GP":
        text = str("Guadaloupe %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        b=  blue
                
        Guadaloupe  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Guadaloupe)

    elif countryCode == "GQ":
        text = str("Equatorial Guinea %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        w = white
        b = blue
        r = red

        EqGuinea =[
        b,g,g,g,g,g,g,g,
        b,b,g,g,g,g,g,g,
        b,b,b,w,w,w,w,w,
        b,b,b,b,w,w,g,w,
        b,b,b,b,w,w,g,w,
        b,b,b,w,w,w,w,w,
        b,b,r,r,r,r,r,r,
        b,r,r,r,r,r,r,r]
        sense.set_pixels(EqGuinea)

    elif countryCode == "GR":
        text = str("Greece %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        B = blue
        W = white

        Greece = [ 
        B,W,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        B,W,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        W,W,W,W,W,W,W,W,
        ]
        sense.set_pixels(Greece)

    elif countryCode == "GT":
        text = str("Guatamala %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue 
        O = white 
        b=  blue
        Y = yellow
                
        Guatamala  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,Y,O,X,X,
        b,b,b,O,Y,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Guatamala)

    elif countryCode == "GU":
        text = str("Guam %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        b = blue
        s = skyblue
        y = yellow

        Guam = [
        r,r,r,r,r,r,r,r,
        r,b,b,b,b,b,b,r,
        r,b,b,s,s,b,b,r,
        r,b,b,s,s,b,b,r,
        r,b,b,s,s,b,b,r,
        r,b,b,y,y,b,b,r,
        r,b,b,b,b,b,b,r,
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Guam)

    elif countryCode == "HK":
        text = str("Hong Kong %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "HM":
        text = str("Heard Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "HN":
        text = str("Honduras %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "HR":
        text = str("Croatia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        R = red
        W = white
        B = blue

        Croatia = [ 
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        W,W,W,W,W,W,W,W,
        W,W,W,R,R,W,W,W,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        ]
        sense.set_pixels(Croatia)        

    elif countryCode == "HT":
        text = str("Haiti %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "HU":
        text = str("Hungary %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        O = white
        X = red
        T = green

        Hungary = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        T,T,T,T,T,T,T,T,
        T,T,T,T,T,T,T,T,
        T,T,T,T,T,T,T,T,
        ]
        sense.set_pixels(Hungary)
        

    elif countryCode == "ID":
        text = str("Indonesia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = white
                
        Indonesia = [
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Indonesia)    

    elif countryCode == "IE":
        text = str("Ireland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = orange
        O = white 
        b=  green
                
        Ireland  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Ireland)
        
    elif countryCode == "IL":
        text = str("Israel %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "IN":
        text = str("India %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        x = orange
        w = white
        o = green
        k = blue
                
        India = [
        x,x,x,x,x,x,x,x,
        x,x,x,x,x,x,x,x,
        w,w,w,w,w,w,w,w,
        w,w,w,k,k,w,w,w,
        w,w,w,k,k,w,w,w,
        w,w,w,w,w,w,w,w,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o]
        sense.set_pixels(India)

    elif countryCode == "IQ":
        text = str("Iraq %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        R = red
        B = black
        W = white
        G = green

        Iraq = [ 
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        W,W,W,W,W,W,W,W,
        W,G,W,W,G,G,W,W,
        W,W,G,W,W,W,G,W,
        W,W,W,W,W,W,W,W,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B]
        sense.set_pixels(Iraq)

    elif countryCode == "IR":
        text = str("Iran %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = white
        V = green
        B = black

        Iran = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,V,V,V,V,O,O,
        O,O,V,V,V,V,O,O,
        O,O,O,O,O,O,O,O,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B]
        sense.set_pixels(Iran) 

    elif countryCode == "IS":
        text = str("Iceland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "IT":
        text = str("Italy %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white
        G = green 

        Italy = [ 
        G,G,G,O,O,X,X,X,
        G,G,G,O,O,X,X,X,
        G,G,G,O,O,X,X,X,
        G,G,G,O,O,X,X,X,
        G,G,G,O,O,X,X,X,
        G,G,G,O,O,X,X,X,
        G,G,G,O,O,X,X,X,
        G,G,G,O,O,X,X,X] 
        sense.set_pixels(Italy)
 
    elif countryCode == "JE":
        text = str("Jersey %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "JM":
        text = str("Jamaica %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "JO":
        text = str("Jordan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "JF":
        text = str("Japan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = white

        Japan = [
        O,O,O,O,O,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,X,X,X,X,O,O,
        O,X,X,X,X,X,X,O,
        O,X,X,X,X,X,X,O,
        O,O,X,X,X,X,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Japan)

    elif countryCode == "KE":
        text = str("Kenya %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "KG":
        text = str("Kyrgyzstan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "KH":
        text = str("Cambodia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "KI":
        text = str("Kiribati %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "KM":
        text = str("Comoros %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "KP":
        text = str("Korea %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = blue 
        Y = white
        Z = black

        Korea = [ 
        Y,Y,Z,Y,Y,Z,Y,Y,
        Y,Z,Y,Y,Y,Y,Z,Y,
        Z,Y,Y,Y,Y,Y,Y,Z,
        Y,Y,Y,X,X,Y,Y,Y,
        Y,Y,Y,X,X,Y,Y,Y,
        Z,Y,Y,Y,Y,Y,Y,Z,
        Y,Z,Y,Y,Y,Y,Z,Y,
        Y,Y,Z,Y,Y,Z,Y,Y,
        ]
        sense.set_pixels(Korea) 

    elif countryCode == "KW":
        text = str("Kuwait %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "KY":
        text = str("Cayman Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "KZ":
        text = str("Kazakhstan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        Z = yellow
        H = [23, 166, 255]
        
        kaz = [
        H,Z,H,H,H,H,H,H,
        H,Z,H,H,H,H,H,H,
        H,Z,H,H,Z,Z,H,H,
        H,Z,H,Z,Z,Z,Z,H,
        H,Z,H,Z,Z,Z,Z,H,
        H,Z,H,H,Z,Z,H,H,
        H,Z,H,H,H,H,H,H,
        H,Z,H,H,H,H,H,H,]
        sense.set_pixels(kaz)

    elif countryCode == "LA":
        text = str("Laos %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LB":
        text = str("Lebanon %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LC":
        text = str("Saint Lucia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LI":
        text = str("Liechtenstein %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LE":
        text = str("Sri Lanka %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LR":
        text = str("Liberia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LS":
        text = str("Lesotho %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LT":
        text = str("Lithuania %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LU":
        text = str("Luxembourg %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LV":
        text = str("Latvia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "LY":
        text = str("Lybia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        O = black
        Z = yellow
        R = white
        V = red

        Lybia = [
        V,V,V,V,V,V,V,V,
        V,V,V,V,V,V,V,V,
        O,O,O,R,O,O,O,O,
        O,O,R,O,O,R,O,O,
        O,O,R,O,O,O,O,O,
        O,O,O,R,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Lybia)

    elif countryCode == "MA":
        text = str("Morocco %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MC":
        text = str("Monaco %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MD":
        text = str("Moldova %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = yellow
        b = blue
        Z = black
                
        Moldova  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,Z,O,X,X,
        b,b,b,O,Z,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Moldova)
        
    elif countryCode == "ME":
        text = str("Montenegro %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MF" or countryCode == "SX":
        text = str("St Martin %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        b=  blue
                
        StMartin  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(StMartin)
 
    elif countryCode == "MG":
        text = str("Madagascar %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MH":
        text = str("Marshal Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MK":
        text = str("Macedonia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "ML":
        text = str("Mali %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        Y = red
        Z = yellow

        Mali = [
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z,
        X,X,X,Y,Y,Z,Z,Z]
        sense.set_pixels(Mali)

    elif countryCode == "MM":
        text = str("Myanmar %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        y = yellow
        g = green
        r = red
        w = white

        Myanmar = [
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        g,g,g,w,w,g,g,g,
        g,g,w,w,w,w,g,g,
        g,g,g,w,w,g,g,g,
        r,r,w,r,r,w,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Myanmar)
        
    elif countryCode == "MN":
        text = str("Mongolia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = blue
        Z = yellow

        Mongolia = [
        X,X,X,O,O,X,X,X,
        X,Z,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,Z,X,O,O,X,X,X,
        X,Z,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,Z,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X]
        sense.set_pixels(Mongolia)

    elif countryCode == "MO":
        text = str("Macao %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MQ":
        text = str("Martinique %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        b = blue
                
        Martinique  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Martinique)

    elif countryCode == "MR":
        text = str("Mauritania %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green 
        O = yellow 
        T = black

        Mauritania = [ 
        X,X,X,X,X,X,X,X,
        X,O,X,O,X,O,X,X,
        X,O,X,X,X,O,X,X,
        X,X,O,X,O,X,X,X,
        X,X,X,O,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X] 
        sense.set_pixels(Mauritania) 

    elif countryCode == "MS":
        text = str("Montserrat %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MT":
        text = str("Malta %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MU":
        text = str("Mauritius %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MV":
        text = str("Maldives %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MW":
        text = str("Malawi %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "MX":
        text = str("Mexico %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        b = green
        Y = yellow
                
        Mexico  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,Y,O,X,X,
        b,b,b,O,Y,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Mexico)
        
    elif countryCode == "MY":
        text = str("Malaysia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = turquoise  
        O = yellow 
        T = black

        Malaysia = [ 
        T,X,X,X,X,X,X,X,
        T,T,X,X,X,X,X,X,
        T,T,T,X,X,X,X,X,
        T,T,T,T,O,O,O,O,
        T,T,T,T,O,O,O,O,
        T,T,T,X,X,X,X,X,
        T,T,X,X,X,X,X,X,
        T,X,X,X,X,X,X,X] 
        sense.set_pixels(Malaysia)
        
    elif countryCode == "MZ":
        text = str("Mozambique %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "NA":
        text = str("Namibia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = yellow 
        T = blue

        Namibia = [ 
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X,
        T,T,T,O,O,X,X,X]
        sense.set_pixels(Namibia)

    elif countryCode == "NC":
        text = str("New Caledonia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "NE":
        text = str("Niger %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        W = white
        Z = orange

        Niger = [
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        W,W,W,W,W,W,W,W,
        W,W,W,Z,Z,W,W,W,
        W,W,W,Z,Z,W,W,W,
        W,W,W,W,W,W,W,W,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Niger)

    elif countryCode == "NF":
        text = str("Norfolk Island %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "NG":
        text = str("Nigeria %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = green
        O = white 
        X = green

        Nigeria = [
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Nigeria)

    elif countryCode == "NI":
        text = str("Nicaragua %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        w = white
        g = green

        Nicaragua = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        w,w,w,w,w,w,w,w,
        w,w,w,g,g,w,w,w,
        w,w,g,g,g,g,w,w,
        w,w,w,w,w,w,w,w,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b]
        sense.set_pixels(Nicaragua)

    elif countryCode == "NL":
        text = str("Netherlands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white
        O = red
        Z = blue

        Netherlands = [
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z,
        Z,Z,Z,Z,Z,Z,Z,Z]
        sense.set_pixels(Netherlands)

    elif countryCode == "NO":
        text = str("Norway %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "NP":
        text = str("Nepal %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "NR":
        text = str("Nauru %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "NU":
        text = str("Niue %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "NZ":
        text = str("New Zealand %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        R = red 
        B = blue 
        W = white

        New_Zealand = [ 
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,W,B,B,
        B,B,B,B,B,B,R,B,
        B,B,B,B,W,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,R,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B]
        sense.set_pixels(New_Zealand)

    elif countryCode == "OM":
        text = str("Oman %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "PA":
        text = str("Panama %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "PE":
        text = str("Peru %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = white  
        T = black

        Peru = [ 
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X,
        X,X,X,O,O,X,X,X]
        sense.set_pixels(Peru)

    elif countryCode == "PF":
        text = str("Fr. Polynesia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "PG":
        text = str("Papua Guinea %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "PH":
        text = str("Philippines %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        B = blue
        R = red  
        W = white  
        Y = yellow

        Philippines = [ 
        W,B,B,B,B,B,B,B,
        W,W,B,B,B,B,B,B,
        W,W,W,B,B,B,B,B,
        W,Y,Y,W,B,B,B,B,
        W,Y,Y,W,R,R,R,R,
        W,W,W,R,R,R,R,R,
        W,W,R,R,R,R,R,R,
        W,R,R,R,R,R,R,R]
        sense.set_pixels(Philippines)

    elif countryCode == "PK":
        text = str("Pakistan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = darkgreen 
        O = white 

        Pakistain = [ 
        O,O,X,X,X,X,X,X,
        O,O,X,X,O,X,X,X,
        O,O,X,O,X,X,O,X,
        O,O,X,O,X,X,X,X,
        O,O,X,O,X,X,O,X,
        O,O,X,X,O,O,X,X,
        O,O,X,X,X,X,X,X,
        O,O,X,X,X,X,X,X,]
        sense.set_pixels(Pakistain)

    elif countryCode == "PL":
        text = str("Poland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        W = white
        R = red

        Poland = [
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R,
        R,R,R,R,R,R,R,R]
        sense.set_pixels(Poland)

    elif countryCode == "PN":
        text = str("Pitcairn %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "PR":
        text = str("Puerto Rico %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        w = white
        b = blue

        PuertoRico = [
        b,r,r,r,r,r,r,r,
        b,b,r,r,r,r,r,r,
        b,b,b,w,w,w,w,w,
        b,w,w,b,w,w,w,w,
        b,w,w,b,r,r,r,r,
        b,b,b,r,r,r,r,r,
        b,b,w,w,w,w,w,w,
        b,r,r,r,r,r,r,r]
        sense.set_pixels(PuertoRico)

    elif countryCode == "PS":
        text = str("Palestine %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "PT":
        text = str("Portugal %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        r = red 
        y = yellow 
                
        Portugal  = [ 
        g,g,g,r,r,r,r,r,
        g,g,g,r,r,r,r,r,
        g,y,y,y,r,r,r,r,
        g,y,r,y,r,r,r,r,
        g,y,y,y,r,r,r,r,
        g,g,g,r,r,r,r,r,
        g,g,g,r,r,r,r,r,
        g,g,g,r,r,r,r,r]
        sense.set_pixels(Portugal)

    elif countryCode == "PW":
        text = str("Palau %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "PY":
        text = str("Paraguay %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        r = red 
        b = blue
        w = white
                
        Paraguay = [ 
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        w,w,w,w,w,w,w,w,
        w,w,w,g,g,w,w,w,
        w,w,w,w,w,w,w,w,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b]
        sense.set_pixels(Paraguay)

    elif countryCode == "QA":
        text = str("Qatar %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "RE":
        text = str("Reunion %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        b = blue
                
        Reunion  = [ 
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X,
        b,b,b,O,O,O,X,X]
        sense.set_pixels(Reunion)

    elif countryCode == "RO":
        text = str("Romania %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue    
        O = yellow  
        T = red 

        Romania = [  
        X,X,X,O,O,T,T,T,
        X,X,X,O,O,T,T,T,
        X,X,X,O,O,T,T,T,
        X,X,X,O,O,T,T,T,
        X,X,X,O,O,T,T,T,
        X,X,X,O,O,T,T,T,
        X,X,X,O,O,T,T,T,
        X,X,X,O,O,T,T,T ]
        sense.set_pixels(Romania)

    elif countryCode == "RS":
        text = str("Serbia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = white 
        O = red 
        Y = blue
        G = yellow
             
        Serbia = [ 
        O,O,O,O,O,O,O,O,
        O,O,G,O,O,O,O,O,
        O,G,G,G,O,O,O,O,
        Y,X,X,X,Y,Y,Y,Y,
        Y,X,X,X,Y,Y,Y,Y,
        X,O,X,O,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Serbia)
        

    elif countryCode == "RU":
        text = str("Russian Federation %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        Y = blue
             
        Russia = [ 
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        Y,Y,Y,Y,Y,Y,Y,Y,
        Y,Y,Y,Y,Y,Y,Y,Y,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Russia)

    elif countryCode == "RW":
        text = str("Rwanda %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SA":
        text = str("Saudi Arabia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        O = white

        SaudiArabia = [
        X,X,X,X,X,X,X,X,
        X,O,X,O,O,O,X,X,
        X,O,O,O,O,O,O,X,
        X,O,O,O,X,X,X,X,
        X,X,X,X,X,O,X,X,
        X,O,O,O,O,O,O,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(SaudiArabia)

    elif countryCode == "SB":
        text = str("Solomon Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SC":
        text = str("Seychelles %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SD":
        text = str("Sudan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SE":
        text = str("Sweden %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        y = yellow

        Sweden = [
        b,b,y,y,b,b,b,b,
        b,b,y,y,b,b,b,b,
        b,b,y,y,b,b,b,b,
        y,y,y,y,y,y,y,y,
        y,y,y,y,y,y,y,y,
        b,b,y,y,b,b,b,b,
        b,b,y,y,b,b,b,b,
        b,b,y,y,b,b,b,b]
        sense.set_pixels(Sweden)        

    elif countryCode == "SG":
        text = str("Singapore %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SH":
        text = str("St Helena %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SI":
        text = str("Slovenia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        Y = blue
             
        Slovenia = [ 
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,Y,Y,O,O,O,O,
        Y,Y,O,O,Y,Y,Y,Y,
        Y,Y,Y,Y,Y,Y,Y,Y,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Slovenia)

    elif countryCode == "SK":
        text = str("Slovakia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = white
        V = blue
                 
        Slovakia = [ 
        O,O,O,O,O,O,O,O,
        O,X,X,X,O,O,O,O,
        O,X,O,X,O,O,O,O,
        V,O,O,O,V,V,V,V,
        V,X,V,X,V,V,V,V,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(Slovakia)

    elif countryCode == "SL":
        text = str("Sierra Leone %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SM":
        text = str("San Marino %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SN":
        text = str("Senegal %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "SO":
        text = str("Somalia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = skyblue
        w = white

        Somalia = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,w,w,b,b,b,
        b,b,w,w,w,w,b,b,
        b,b,b,w,w,b,b,b,
        b,b,w,b,b,w,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b]
        sense.set_pixels(Somalia)
        
    elif countryCode == "SR":
        text = str("Suriname %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        w = white
        r = red
        y = yellow

        Suriname = [
        g,g,g,g,g,g,g,g,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        r,r,r,y,y,r,r,r,
        r,r,r,y,y,r,r,r,
        r,r,r,r,r,r,r,r,
        w,w,w,w,w,w,w,w,
        g,g,g,g,g,g,g,g]        
        sense.set_pixels (Suriname)

    elif countryCode == "SS":
        text = str("South Sudan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = white
                
        Sudan = [
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O,
        O,O,O,X,X,O,O,O]
        sense.set_pixels (Sudan)

    elif countryCode == "SV":
        text = str("El Salvador %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        w = white

        Salvador = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        w,w,w,w,w,w,w,w,
        w,w,w,b,b,w,w,w,
        w,w,w,w,w,w,w,w,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b]
        sense.set_pixels (Salvador)

    elif countryCode == "SZ":
        text = str("Swaziland %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "TD":
        text = str("Chad %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red
        O = blue
        Z = yellow

        Chad = [
        O,O,Z,Z,Z,Z,X,X,
        X,O,Z,Z,Z,Z,X,X,
        X,O,Z,Z,Z,Z,X,X,
        Z,O,Z,Z,Z,Z,X,X,
        Z,O,Z,Z,Z,Z,X,X,
        X,X,Z,Z,Z,Z,X,X,
        X,X,Z,Z,Z,Z,X,X,
        X,X,Z,Z,Z,Z,X,X]
        sense.set_pixels(Chad)

    elif countryCode == "TF":
        text = str("French Soutern Territories %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        w = white
        r = red

        fst =[
        b,w,r,b,b,b,b,b,
        b,w,r,b,b,b,b,b,
        b,w,r,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,w,w,w,w,b,
        b,b,b,b,w,w,w,b,
        b,b,b,b,b,w,b,b,
        b,b,b,b,b,b,b,b]
        sense.set_pixels(fst)
        
    elif countryCode == "TG":
        text = str("Togo %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "TH":
        text = str("Thailand %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue 
        O = white 
        T = red

        Thailand = [ 
        T,T,T,T,T,T,T,T,
        T,T,T,T,T,T,T,T,
        O,O,O,O,O,O,O,O,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        T,T,T,T,T,T,T,T,]
        sense.set_pixels(Thailand) 

    elif countryCode == "TJ":
        text = str("Tajikistan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        w = white
        g = green
        y = yellow

        Tajikistan = [ 
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        w,w,w,w,w,w,w,w,
        w,w,w,y,y,w,w,w,
        w,w,w,y,y,w,w,w,        
        w,w,w,w,w,w,w,w,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g]
        sense.set_pixels(Tajikistan) 

    elif countryCode == "TK":
        text = str("Tokelau %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "TL":
        text = str("Timor Leste %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "TM":
        text = str("Turkmenistan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = green
        O = blue
        Z = yellow
        U = red
        I = white

        Turkmenistan = [
        X,U,I,U,X,X,X,X,
        X,U,U,U,I,X,I,X,
        X,U,X,U,X,I,X,I,
        X,U,U,U,I,I,X,I,
        X,U,X,U,X,X,I,X,
        X,U,U,U,X,X,X,X,
        X,U,X,U,X,X,X,X,
        X,U,U,U,X,X,X,X]
        sense.set_pixels(Turkmenistan)

    elif countryCode == "TN":
        text = str("Tunisia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        w = white

        Tunisia = [
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,w,w,r,r,r,
        r,r,w,w,r,w,r,r,
        r,r,r,w,w,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Tunisia)

    elif countryCode == "TO":
        text = str("Tonga %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "TR":
        text = str("Turkey %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        x = red
        o = yellow

        Turkey = [
        x,x,x,x,x,x,x,x,
        x,x,o,o,x,x,x,x,
        x,o,x,x,x,o,x,x,
        x,o,x,x,o,o,o,x,
        x,o,x,x,x,o,x,x,
        x,x,o,o,x,x,x,x,
        x,x,x,x,x,x,x,x,
        x,x,x,x,x,x,x,x]
        sense.set_pixels(Turkey)

    elif countryCode == "TT":
        text = str("Trinidad %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        w = white
        b = black

        Trinidad = [
        w,b,w,r,r,r,r,r,
        r,w,b,w,r,r,r,r,
        r,w,b,w,r,r,r,r,
        r,r,w,b,w,r,r,r,
        r,r,r,w,b,w,r,r,
        r,r,r,r,w,b,w,r,
        r,r,r,r,w,b,w,r,
        r,r,r,r,r,w,b,w]
        sense.set_pixels(Trinidad)

    elif countryCode == "TV":
        text = str("Tuvalu %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "TW":
        text = str("Taiwan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        b = blue
        w = white

        Taiwan = [
        b,b,b,b,r,r,r,r,
        b,w,w,b,r,r,r,r,
        b,w,w,b,r,r,r,r,
        b,b,b,b,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Taiwan)
        
    elif countryCode == "TZ":
        text = str("Tanzania %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        y = yellow
        z = black
        b = skyblue

        Tanzania = [
        g,g,g,g,g,y,z,z,
        g,g,g,g,y,z,z,y,
        g,g,g,y,z,z,y,b,
        g,g,y,z,z,y,b,b,
        g,y,z,z,y,b,b,b, 
        y,z,z,y,b,b,b,b,
        z,z,y,b,b,b,b,b,
        z,y,b,b,b,b,b,b]
        sense.set_pixels(Tanzania)
        
    elif countryCode == "UA":
        text = str("Ukraine %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = blue  
        O = yellow 

        Ukraine = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O]
        sense.set_pixels(Ukraine)

    elif countryCode == "UG":
        text = str("Uganda %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = black
        y = yellow
        r = red
        w = white

        Uganda = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        y,y,y,y,y,y,y,y,
        r,r,r,w,w,r,r,r,
        b,b,b,w,w,b,b,b,
        y,y,y,y,y,y,y,y,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Uganda)

    elif countryCode == "US":
        text = str("USA %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red 
        O = white 
        W = blue

        USA = [ 
        O,W,O,W,W,W,W,W,
        W,O,W,X,X,X,X,X,
        O,W,O,W,W,W,W,W,
        X,X,X,X,X,X,X,X,
        W,W,W,W,W,W,W,W,
        X,X,X,X,X,X,X,X,
        W,W,W,W,W,W,W,W,
        X,X,X,X,X,X,X,X]
        sense.set_pixels(USA)

    elif countryCode == "UY":
        text = str("Uruguay %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        b = blue
        w = white
        y = yellow

        Uruguay = [
        w,w,w,b,b,b,b,b,
        w,y,w,w,w,w,w,w,
        w,y,w,b,b,b,b,b,
        w,w,w,w,w,w,w,w,
        b,b,b,b,b,b,b,b,
        w,w,w,w,w,w,w,w,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b]
        sense.set_pixels(Uruguay)

    elif countryCode == "UZ":
        text = str("Uzbekistan %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "VA":
        text = str("Holy See %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "VE":
        text = str("Venezuela %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = yellow
        L = blue
        P = white 

        Venezuela = [ 
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,
        L,L,P,P,P,P,L,L,
        L,P,L,L,L,L,P,L,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X] 
        sense.set_pixels(Venezuela) 

    elif countryCode == "VG":
        text = str("Virgin Islands %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "VN":
        text = str("Vietnam %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        r = red
        y = yellow

        Vietnam = [
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,y,y,r,r,r,
        r,r,y,y,y,y,r,r,
        r,r,r,y,y,r,r,r,
        r,r,y,r,r,y,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r]
        sense.set_pixels(Vietnam)

    elif countryCode == "WS":
        text = str("Samoa %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

    elif countryCode == "YE":
        text = str("Yemen %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        X = red  
        O = white 
        B = black
             
        Yemen = [ 
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        X,X,X,X,X,X,X,X,
        O,O,O,O,O,O,O,O,
        O,O,O,O,O,O,O,O,  
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B] 
        sense.set_pixels(Yemen)

    elif countryCode == "ZA":
        text = str("South Africa %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        x = green
        o = black
        z = yellow
        r = red
        b = blue
        w = white

        SouthAfrica = [
        x,x,w,r,r,r,r,r,
        x,x,x,w,r,r,r,r,
        z,x,x,x,w,w,w,w,
        o,z,x,x,x,x,x,x,
        o,z,x,x,x,x,x,x,
        z,x,x,x,w,w,w,w,
        x,x,x,w,b,b,b,b,
        x,x,x,w,b,b,b,b]
        sense.set_pixels(SouthAfrica)

    elif countryCode == "ZM":
        text = str("Zambia %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        r = red
        b = black
        o = orange

        Zambia = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,o,o,o,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,r,b,o,
        g,g,g,g,g,r,b,o,
        g,g,g,g,g,r,b,o,
        g,g,g,g,g,r,b,o,
        g,g,g,g,g,r,b,o]
        sense.set_pixels(Zambia)

    elif countryCode == "ZW":
        text = str("Zimbabwe %s %s " % (timeZone,daylight))
        sense.show_message(text,text_colour=yellow,back_colour=black)

        g = green
        y = yellow
        r = red
        b = black
        w = white

        Zimbabwe = [
        w,g,g,g,g,g,g,g,
        w,w,y,y,y,y,y,y,
        w,r,w,r,r,r,r,r,
        w,y,r,w,b,b,b,b,
        w,y,y,w,b,b,b,b,
        w,y,w,r,r,r,r,r,
        w,w,y,y,y,y,y,y,
        w,g,g,g,g,g,g,g]
        sense.set_pixels(Zimbabwe)
