from Processing import *
window (500,500)
rectMode(CORNER)
fill(0, 0, 255)
rect(0, 0, 166.66, 150)
fill(255,0,0)
rect(167,0,166.66,150)
fill(0,255,0)
rect(333,0,166.66,150)



def doMouseDragged():
    if mouseY()>175:
       line(pmouseX(), pmouseY(), mouseX(), mouseY())
onMouseDragged += doMouseDragged

def doMouseClicked():
    print( 'mouse clicked at ' + str(mouseX()) + ', ' + str(mouseY()) )
    x = mouseX() 
    y = mouseY()
    if x>0 and x<167 and y>0 and y<150:
        blue = color(0,0,255)
        stroke(blue)
    if x>167 and x<333 and y>0 and y<150:
       red = color(255,0,0)
       stroke(red) 
    if x>333 and y>0 and y<150:
       green = color(0,255,0)
       stroke(green)
    else:
        color(255,255,255)
onMouseClicked += doMouseClicked
