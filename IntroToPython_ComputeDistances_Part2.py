import math
import random

#program input
x1= random.randint(0,4)
y1= random.randint(0, 4)
x2= random.randint(0, 4)
y2= random.randint(0, 4)

#program processing
euclideanDistance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
manhattanDistance = abs(x1-x2) + abs(y1-y2)

#program output

s1 = "(X1,Y1) = ({:d} , {:d}) " .format(x1, y1)
s2 = "(X2,Y2) = ({:d} , {:d}) " .format (x2, y2)
s3 = "Manhattan Distance = {:.3f}" .format(manhattanDistance)
s4 = "Euclidian Distance = {:.3f}" .format(euclideanDistance)

'''
print(s1)
print(s2)
print(s3)
print(s4)
'''

"""
#0- Read and understand this python program. As usual, please have
    one of you share their screen so that you may all collaborate together. 

#1- Reproduce the same output produced by this program only using a SINGLE
     print statement this (will need to use \n newline character --- HAVE FUN!!!)

#2- Instead of asking the user to input the coordinates for the two points, change
    the program to generate random integer values between 0 and 4 for each
    of the coordinates and then proceed to do computations and to print as before.

#3- Have your program print out which of the two computed distances is larger and by how
    much. For example, if Manhattan = 12 and Euclidean = 8.5, program should output:
    
        Manhattan is larger by 3.5

#4- Finally, change your program to recognize cases when the two distances end up
    being the equal and report that as a tie.
"""

print('{}\n{}\n{}\n{}'.format(s1, s2, s3, s4))

if manhattanDistance > euclideanDistance:
    print("The Manhatten Distance is greater by {:.2f}".format(manhattanDistance - euclideanDistance))
elif manhattanDistance == euclideanDistance:
    print("The two distances are equal.")
else:
    print("The Euclidean Distance is greater by {:.2f}".format(-manhattanDistance + euclideanDistance))


