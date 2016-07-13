from Myro import *
init ("sim")
penDown()
#Makes Robot Walk Right#
def walkRight():
    motors (1,0,.35)
    wait (.5)
#Makes Robot Walk Left#    
def walkLeft():
    motors (0,1,.35)
    wait(.5)
#Makes Robot Spin#
def spin1():
    motors (1,-2,22)
#Makes Robot Move Foward & Shake Left & Right#   
def shake1():
    shake1=0
    while shake1<2:
        forward (1,1.35)
        motors (-1,1,.35)
        motors (2,-2,.35)
        shake1=shake1+1
#Makes Robot Move Backwards & Shake Left & Right#
def shake2():
    shake2=0
    while shake2<2:
        backward (1,1.35)
        motors (-1,1,.35)
        motors (2,-2,.35)
        shake2=shake2+1
#Makes Robot Spin Again#        
def spin2():
    motors (1,-2,6)
 #Makes Robot Pause#   
def pause():
    wait (2)
#The Dance Intro#
def intro():
    i=0        
    while i<7:
        walkRight()
        walkLeft()
        i=i+1

intro()
spin1()  
shake1()
shake2()
spin2()
pause()
shake1()
shake2()
