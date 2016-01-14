import turtle               #import functions associated with the turtle library

linelength = int(input('Enter line length '))   #prompt user for line length and cast to int

while linelength != 0:                          #repeat loop until 0 entered as line length
    angle = int(input('Enter angle '))  
    turtle.forward(linelength)                  #.forward function to draw line 
    turtle.right(angle)                         #.right rotate the direction of the turtle
    linelength = int(input('Enter line length '))
    

print ("goodbye")