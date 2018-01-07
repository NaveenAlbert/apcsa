#Project 15A - Naveen Albert
#Geometry Calculator

import math #import math so operations can be performed
print "Geometry Calculator"
print ""

def chooseProgram(): #user has 4 different programs to choose from
    print "Enter 1 to calculate the area of an equalateral triangle"
    print "Enter 2 to calculate the area of a regular polygon"
    print "Enter 3 to calculate angle measures of a regular polygon"
    print "Enter 4 to calculate the number of diagonals in a regular polygon"
    print "Enter 0 to Exit"
    choice = int(raw_input()) #user is prompted for which program to run
    if choice == 1:
        triangle()
    elif choice == 2:
        area()
    elif choice == 3:
        angles()
    elif choice == 4:
        diagonals()
    elif choice == 0:
        exit()
    else:
        print "Invalid choice."
        chooseProgram() #If user enters an invalid option, prompt again
def triangle():
    print "Calculate the area of an equalateral triangle"
    s = int(raw_input("Side length:")) #Get side length from user
    area = ((s**2)*(math.sqrt(3)))/(4) #Perform operations to calculate area
    print ""
    print "The area of an equalateral triangle with side length " + str(s) + " is " + str(area) + "." #Cast integers to string and output string to user
    print ""
    chooseProgram()
def area():
    print "Calculate the area of a regular polygon"
    n = int(raw_input("Number of sides:")) #Get number of sides from user
    s = int(raw_input("Side length:")) #Get side length from user
    area = (n * (s**2))/(4 * math.tan(math.radians(180/n))) #Use tangent and radians from math library
    print ""
    print "The area of a regular polygon with " + str(n) + " sides and side lengths of " + str(s) + " is " + str(area) + "." #Cast integers to string and output string to user
    print ""
    chooseProgram()
def angles():
    print "Calculate angle measures of a regular polygon"
    n = int(raw_input("Number of sides:"))
    totalAngles = 180 * (n-2) #Total angles = entire polygon
    eachAngle = totalAngles/n #Each Angle = number of degrees for entire polygon divided by number of sides
    print ""
    print "If a regular polygon has " + str(n) + " sides, then there will be " + str(totalAngles) + " total degrees and each angle will measure " + str(eachAngle) + " degrees." #Cast integers to string and output string to user
    print ""
    chooseProgram()
def diagonals():
    print "Calculate the number of diagonals in a regular polygon"
    n = int(raw_input("Number of sides:"))
    diagonals = (n * (n-3))/2
    print ""
    print "A regular polygon with " + str(n) + " sides will have " + str(diagonals) + " diagonals." #Cast integers to string and output string to user
    print ""
    chooseProgram()
def exit():
    exit #Exit program
chooseProgram() #Function is called when program is run