from Myro import *
init ("sim")
penDown()
shake1=0
while shake1<2:
    forward (1,1.35)
    motors (-1,1,.35)
    motors (2,-2,.35) 
    shake1=shake1+1
shake2=0
while shake2<2:
    forward (1,1.35)
    motors (-1,1,.35)
    motors (2,-2,.35)
    backward (1,1.35)
    motors (-1,1,.35)
    motors (2,-2,.35)
    forward (1,1.35)
    motors (-1,1,.35)
    motors (2,-2,.35)
    shake2=shake2+1
motors (1,-1,4)

