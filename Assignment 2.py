"""
# Name: Eric Ortiz
# Student Number: 102-39-903
# Date: 12/19/17
# Assignment #2
# Desc: This program is a basic graphics engine that can display a 3D pyramid on a 2D coordinate plane. There are
        a handful of tools also provided that allow the user to translate, scale, and rotation the pyramid -- along
        with a reset button.
"""

import math
from tkinter import *

CanvasWidth = 400
CanvasHeight = 400
d = 500

# ***************************** Initialize Object Classes ***************************
class Pyramid:
    # The default constructor accepts five vertices
    def __init__(self, apex=None, base1=None, base2=None, base3=None, base4=None):
        # If no vertices are passed in, then we use the original default values
        if apex is None:
            # These vertices are mutated by different functions outside of the class
            self.apex = [0, 50, 100]
            self.base1 = [-50, -50, 50]
            self.base2 = [50, -50, 50]
            self.base3 = [50, -50, 150]
            self.base4 = [-50, -50, 150]
            # These vertices are never touched so that they are used only for resetting the object to its original
            # position
            self.defaultapex = [0, 50, 100]
            self.defaultbase1 = [-50, -50, 50]
            self.defaultbase2 = [50, -50, 50]
            self.defaultbase3 = [50, -50, 150]
            self.defaultbase4 = [-50, -50, 150]
        # If vertices are passed in, then assign them to the object's built-in vertices
        else:
            self.apex = apex
            self.base1 = base1
            self.base2 = base2
            self.base3 = base3
            self.base4 = base4
            # Also store them for the reset function in these variables. The list() function makes sure that these
            # variables are creating new instances of the passed in values, so that it is no longer being passed in by
            # reference.
            self.defaultapex = list(apex)
            self.defaultbase1 = list(base1)
            self.defaultbase2 = list(base2)
            self.defaultbase3 = list(base3)
            self.defaultbase4 = list(base4)

        # Once the vertices are created, we make the polygons of the pyramid
        self.frontpoly = [self.apex, self.base1, self.base2]
        self.rightpoly = [self.apex, self.base2, self.base3]
        self.backpoly = [self.apex, self.base3, self.base4]
        self.leftpoly = [self.apex, self.base1, self.base4]
        # Because the base of the pyramid is a square, we break that face into two triangular polygons
        self.bottompoly1 = [self.base1, self.base2, self.base4]
        self.bottompoly2 = [self.base2, self.base3, self.base4]

        # Finally we create the shape and the object's pointcloud
        self.shape = [self.bottompoly1, self.bottompoly2, self.frontpoly, self.rightpoly, self.backpoly, self.leftpoly]
        self.pointcloud = [self.apex, self.base1, self.base2, self.base3, self.base4]

    # This function is solely used to reset the object to its original position
    def rebuildShape(self):
        # Set the object's points to the value of the previously stored default ones by using the list() function.
        # That prevents the default vertices from being "tied" to these vertices which will be changed constantly.
        self.apex = list(self.defaultapex)
        self.base1 = list(self.defaultbase1)
        self.base2 = list(self.defaultbase2)
        self.base3 = list(self.defaultbase3)
        self.base4 = list(self.defaultbase4)

        # Now we just rebuild the polygons, the shape, and the pointcloud
        self.frontpoly = [self.apex, self.base1, self.base2]
        self.rightpoly = [self.apex, self.base2, self.base3]
        self.backpoly = [self.apex, self.base3, self.base4]
        self.leftpoly = [self.apex, self.base1, self.base4]
        self.bottompoly1 = [self.base1, self.base2, self.base4]
        self.bottompoly2 = [self.base2, self.base3, self.base4]

        self.shape = [self.bottompoly1, self.bottompoly2, self.frontpoly, self.rightpoly, self.backpoly, self.leftpoly]
        self.pointcloud = [self.apex, self.base1, self.base2, self.base3, self.base4]

    # End Pyramid Class

class Cube:
    # The default constructor accepts eight vertices
    def __init__(self, base1=None, base2=None, base3=None, base4=None, base5=None, base6=None, base7=None, base8=None):
        # If no vertices are passed in, then we use the original default values
        if base1 is None:
            # These vertices are mutated by different functions outside of the class
            self.base1 = [-50, -50, 50]
            self.base2 = [50, -50, 50]
            self.base3 = [50, -50, 150]
            self.base4 = [-50, -50, 150]
            self.base5 = [-50, 50, 50]
            self.base6 = [50, 50, 50]
            self.base7 = [50, 50, 150]
            self.base8 = [-50, 50, 150]
            # These vertices are never touched so that they are used only for resetting the object to its original
            # position
            self.defaultbase1 = [-50, -50, 50]
            self.defaultbase2 = [50, -50, 50]
            self.defaultbase3 = [50, -50, 150]
            self.defaultbase4 = [-50, -50, 150]
            self.defaultbase5 = [-50, 50, 50]
            self.defaultbase6 = [50, 50, 50]
            self.defaultbase7 = [50, 50, 150]
            self.defaultbase8 = [-50, 50, 150]
        # If vertices are passed in, then assign them to the object's built-in vertices
        else:
            self.base1 = base1
            self.base2 = base2
            self.base3 = base3
            self.base4 = base4
            self.base5 = base5
            self.base6 = base6
            self.base7 = base7
            self.base8 = base8
            # Also store them for the reset function in these variables. The list() function makes sure that these
            # variables are creating new instances of the passed in values, so that it is no longer being passed in by
            # reference.
            self.defaultbase1 = list(base1)
            self.defaultbase2 = list(base2)
            self.defaultbase3 = list(base3)
            self.defaultbase4 = list(base4)
            self.defaultbase5 = list(base5)
            self.defaultbase6 = list(base6)
            self.defaultbase7 = list(base7)
            self.defaultbase8 = list(base8)

        # Once the vertices are created, we make the polygons of the pyramid. Since the object is a cube, then every
        # face of it has two polygons - which are just two triangles
        self.frontpoly1 = [self.base1, self.base2, self.base6]
        self.frontpoly2 = [self.base1, self.base5, self.base6]
        self.backpoly1 = [self.base3, self.base4, self.base8]
        self.backpoly2 = [self.base3, self.base7, self.base8]
        self.leftpoly1 = [self.base1, self.base4, self.base5]
        self.leftpoly2 = [self.base4, self.base5, self.base8]
        self.rightpoly1 = [self.base2, self.base3, self.base7]
        self.rightpoly2 = [self.base2, self.base6, self.base7]
        self.bottompoly1 = [self.base1, self.base2, self.base4]
        self.bottompoly2 = [self.base1, self.base3, self.base4]
        self.toppoly1 = [self.base5, self.base6, self.base7]
        self.toppoly2 = [self.base5, self.base7, self.base8]

        # Finally we create the shape and the object's pointcloud
        self.shape = [self.frontpoly1, self.frontpoly2, self.backpoly1, self.backpoly2, self.leftpoly1, self.leftpoly2, \
                      self.rightpoly1, self.rightpoly2, self.bottompoly1, self.bottompoly1, self.toppoly1, self.toppoly2]
        self.pointcloud = [self.base1, self.base2, self.base3, self.base4, self.base5, self.base6, self.base7, self.base8]

    def rebuildShape(self):
        # Set the object's points to the value of the previously stored default ones by using the list() function.
        # That prevents the default vertices from being "tied" to these vertices which will be changed constantly.
        self.base1 = list(self.defaultbase1)
        self.base2 = list(self.defaultbase2)
        self.base3 = list(self.defaultbase3)
        self.base4 = list(self.defaultbase4)
        self.base5 = list(self.defaultbase5)
        self.base6 = list(self.defaultbase6)
        self.base7 = list(self.defaultbase7)
        self.base8 = list(self.defaultbase8)

        # Now we just rebuild the polygons, the shape, and the pointcloud
        self.frontpoly1 = [self.base1, self.base2, self.base6]
        self.frontpoly2 = [self.base1, self.base5, self.base6]
        self.backpoly1 = [self.base3, self.base4, self.base8]
        self.backpoly2 = [self.base3, self.base7, self.base8]
        self.leftpoly1 = [self.base1, self.base4, self.base5]
        self.leftpoly2 = [self.base4, self.base5, self.base8]
        self.rightpoly1 = [self.base2, self.base3, self.base7]
        self.rightpoly2 = [self.base2, self.base6, self.base7]
        self.bottompoly1 = [self.base1, self.base2, self.base4]
        self.bottompoly2 = [self.base1, self.base3, self.base4]
        self.toppoly1 = [self.base5, self.base6, self.base7]
        self.toppoly2 = [self.base5, self.base7, self.base8]

        self.shape = [self.frontpoly1, self.frontpoly2, self.backpoly1, self.backpoly2, self.leftpoly1, self.leftpoly2, \
                      self.rightpoly1, self.rightpoly2, self.bottompoly1, self.bottompoly1, self.toppoly1,
                      self.toppoly2]
        self.pointcloud = [self.base1, self.base2, self.base3, self.base4, self.base5, self.base6, self.base7, self.base8]

# ***************************** Create the Objects ***************************

customCube1 = Cube([150, -50, 50], [250, -50, 50], [250, -50, 150], [150, -50, 150], [150, 50, 50], [250, 50, 50],
                  [250, 50, 150], [150, 50, 150])

customCube2 = Cube([-150, -50, 50], [-250, -50, 50], [-250, -50, 150], [-150, -50, 150], [-150, 50, 50], [-250, 50, 50],
                  [-250, 50, 150], [-150, 50, 150])

currentObject = [Pyramid(), customCube1, customCube2]

objectNumber = 0

# ***************************** Backend Button Functions ***************************

# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud
def resetPyramid(object):
    object.rebuildShape()
    print("resetPyramid stub executed.")


# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.
def translate(object, displacement):
    # iterate through the points in the object
    for i in range(len(object)):
        point = object[i]
        # for every point, add each component with that of the displacement component
        for j in range(len(point)):
            point[j] += displacement[j]

    print("translate stub executed.")


# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.
def scale(object, scalefactor):
    # iterate through the points in the object
    for i in range(len(object)):
        point = object[i]
        # for every point, multiply each component by the scalefactor
        for j in range(len(point)):
            point[j] *= scalefactor

    print("scale stub executed.")


# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard position]
def rotateZ(object, degrees):
    # first convert the degrees to radians
    radians = math.radians(degrees)

    # iterate through the polygons in the object and grab each point
    for i in range(len(object)):
        point = object[i]
        # so that the points don't get manipulated during computation, assign the x and y values separately
        x = point[0]
        y = point[1]
        # use the z-rotation function
        point[0] = (x * math.cos(radians)) - (y * math.sin(radians))
        point[1] = (x * math.sin(radians)) + (y * math.cos(radians))

    print("rotateZ stub executed.")


# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.
def rotateY(object, degrees):
    # first convert the degrees to radians
    radians = math.radians(degrees)

    # iterate through the polygons in the object and grab each point
    for i in range(len(object)):
        point = object[i]
        # so that the points don't get manipulated during computation, assign the x and z values separately
        x = point[0]
        z = point[2]
        # use the y-rotation function
        point[0] = (x * math.cos(radians)) + (z * math.sin(radians))
        point[2] = (-1 * (x * math.sin(radians))) + (z * math.cos(radians))

    print("rotateY stub executed.")


# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.
def rotateX(object, degrees):
    # first convert the degrees to radians
    radians = math.radians(degrees)

    # iterate through the polygons in the object and grab each point
    for i in range(len(object)):
        point = object[i]
        # so that the points don't get manipulated during computation, assign the y and z values separately
        y = point[1]
        z = point[2]
        # use the x-rotation function
        point[1] = (y * math.cos(radians)) - (z * math.sin(radians))
        point[2] = (y * math.sin(radians)) + (z * math.cos(radians))

    print("rotateX stub executed.")


# The function will draw an object by repeatedly calling drawPoly on each polygon in the object
def drawObject(object):
    for i in range(len(object.shape)):
        drawPoly(object.shape[i])
    print("drawObject stub executed.")


# This function will draw a polygon by repeatedly calling drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly):
    for i in range(len(poly)):
        drawLine(poly[i - 1], poly[i])
    print("drawPoly stub executed.")


# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
def drawLine(start, end):
    # first convert the given start and end points to their perspective projection
    startproject = project(start)
    endproject = project(end)

    # then displace the projection points so that the center of the canvas is the origin
    startdisplay = convertToDisplayCoordinates(startproject)
    enddisplay = convertToDisplayCoordinates(endproject)

    # draw the line with the new canvas-centered points
    w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1])
    print("drawLine stub executed.")


# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    # grab the distance of the center of projection from the screen and use it to find the new points for ps
    global d
    # just plug it into the perspective projection formula
    xps = (d * point[0]) / (d + point[2])
    yps = (d * point[1]) / (d + point[2])
    zps = point[2] / (d + point[2])
    # create the new point perspective projection point
    ps = [xps, yps, zps]
    return ps


# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    displayXY = []
    # reorient the components of the point so that the origin is in the center of the canvas with a positive y axis
    displayXY.append(point[0] + CanvasWidth/2)
    displayXY.append(-point[1] + CanvasHeight/2)
    displayXY.append(point[2])
    return displayXY


# ***************************** Interface Functions ***************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    resetPyramid(currentObject[objectNumber])
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def larger():
    w.delete(ALL)
    scale(currentObject[objectNumber].pointcloud, 1.1)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def smaller():
    w.delete(ALL)
    scale(currentObject[objectNumber].pointcloud, .9)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def forward():
    w.delete(ALL)
    translate(currentObject[objectNumber].pointcloud, [0, 0, 5])
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def backward():
    w.delete(ALL)
    translate(currentObject[objectNumber].pointcloud, [0, 0, -5])
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def left():
    w.delete(ALL)
    translate(currentObject[objectNumber].pointcloud, [-5, 0, 0])
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def right():
    w.delete(ALL)
    translate(currentObject[objectNumber].pointcloud, [5, 0, 0])
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def up():
    w.delete(ALL)
    translate(currentObject[objectNumber].pointcloud, [0, 5, 0])
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def down():
    w.delete(ALL)
    translate(currentObject[objectNumber].pointcloud, [0, -5, 0])
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def xPlus():
    w.delete(ALL)
    rotateX(currentObject[objectNumber].pointcloud, 5)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def xMinus():
    w.delete(ALL)
    rotateX(currentObject[objectNumber].pointcloud, -5)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def yPlus():
    w.delete(ALL)
    rotateY(currentObject[objectNumber].pointcloud, 5)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def yMinus():
    w.delete(ALL)
    rotateY(currentObject[objectNumber].pointcloud, -5)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def zPlus():
    w.delete(ALL)
    rotateZ(currentObject[objectNumber].pointcloud, 5)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def zMinus():
    w.delete(ALL)
    rotateZ(currentObject[objectNumber].pointcloud, -5)
    for i in range(len(currentObject)):
        drawObject(currentObject[i])


def nextSelection():
    global objectNumber

    if objectNumber is 2:
        objectNumber = 0
    else:
        objectNumber += 1

    print("nextSelection stub executed.")


def prevSelection():
    global objectNumber

    if objectNumber is -1:
        objectNumber = 1
    else:
        objectNumber -= 1

    print("prevSelection stub executed.")

# ***************************** Interface and Window Construction ***************************
root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
for i in range(len(currentObject)):
    drawObject(currentObject[i])
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="DN", command=down)
upButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

selectcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
selectcontrols.pack(side=LEFT)

selectcontrolslabel = Label(selectcontrols, text="Selection")
selectcontrolslabel.pack()

selectForwardButton = Button(selectcontrols, text="Next", command=nextSelection)
selectForwardButton.pack(side=LEFT)

selectBackwardButton = Button(selectcontrols, text="Previous", command=prevSelection)
selectBackwardButton.pack(side=LEFT)

root.mainloop()

# TODO: Fix it so that when you rotate an object, its along its own axis rather than the world axis. Then make sure the
# TODO: comments are all set and in place