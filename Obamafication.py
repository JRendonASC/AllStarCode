from Myro import *
pict = makePicture("J.JPG")
show(pict)
x = getPixels(pict)

for pixel in x:
    g=getGray(pixel)
    if g>=180:
        setColor(pixel,makeColor(252,227,166))
    elif g>=120:
        setColor(pixel,makeColor(112,150,158))
    elif g>=60:
        setColor(pixel,makeColor(217,26,33))
    else:
        setColor(pixel,makeColor(0,51,76))