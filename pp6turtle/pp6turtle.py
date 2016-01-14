import turtle

linelength = int(input('Enter line length '))

while linelength != 0:
    angle = int(input('Enter angle '))
    turtle.forward(linelength)
    turtle.right(angle)
    linelength = int(input('Enter line length '))
    

print ("goodbye")