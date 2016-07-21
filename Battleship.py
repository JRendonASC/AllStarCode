from Processing import *
from random import *
window (400,400)
width=80
length=80
i=0
while i<5:
    newX=width*i
    line(newX,0,newX,400)
    newY=length*i
    line(0,newY,400,newY)
    i=i+1
    
board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
board[randrange(5)][randrange(5)]=1    

GAMEOVER=False
#row = 0
#column = 0
while GAMEOVER==False: 

    row=int(input("Which Row"))
    column=int(input("Which Column"))
 
    while row>4 or row<0:
        row=int(input("Input New Row Number between 0 and 4"))
    while column>4 or column<0:
        column=int(input("Input New Column Number between 0 and 4"))
    
        
    if board[row][column] ==1: #if user hits ship
        GAMEOVER==True
        input("YOU WON!!!")
    else:
        fill(255,0,0)
        rect(width*column,length*row,80,80)
            