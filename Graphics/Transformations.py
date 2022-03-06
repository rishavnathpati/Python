import math
import numpy as np

n = int(input("Enter the numnber of vertices of the figure: "))
x_points = [0]*n
y_points = [0]*n

for i in range(0, n):
    x_points[i] = int(
        input("Enter the x co-ordinate of point " + str(i+1)+": "))
    y_points[i] = int(
        input("Enter the y co-ordinate of point " + str(i+1)+": "))
    print()


def translation(n, x_points, y_points):

    tx = int(input("Enter the x co-ordinate of the translation vector pair: "))
    ty = int(input("Enter the y co-ordinate of the translation vector pair: "))
    trans_x_points = [0]*n
    trans_y_points = [0]*n

    for i in range(0, n):
        trans_x_points[i] = x_points[i] + tx
        trans_y_points[i] = y_points[i] + ty

    for i in range(0, n):
        print("The translated co-ordinates of point " + str(i+1) +
              " are: (" + str(trans_x_points[i]) + "," + str(trans_y_points[i]) + ")")
        print()


def rotation(n, x_points, y_points):

    t = int(
        input("Enter the angle(in degrees) through which the figure will be rotated: "))
    rad_t = math.radians(t)
    rotation_x_points = [0]*n
    rotation_y_points = [0]*n

    for i in range(0, n):
        rotation_x_points[i] = round(
            x_points[i]*math.cos(rad_t) - y_points[i]*math.sin(rad_t))
        rotation_y_points[i] = round(
            x_points[i]*math.sin(rad_t) + y_points[i]*math.cos(rad_t))

    for i in range(0, n):
        print("The rotated co-ordinates of point " + str(i+1) + " are: (" +
              str(rotation_x_points[i]) + "," + str(rotation_y_points[i]) + ")")
        print()


def scaling(n, x_points, y_points):

    tx = float(input("Enter the x axis scale object: "))
    ty = float(input("Enter the y axis scale object: "))
    scale_x_points = [0]*n
    scale_y_points = [0]*n

    for i in range(0, n):
        scale_x_points[i] = round(x_points[i]*tx)
        scale_y_points[i] = round(y_points[i]*ty)

    for i in range(0, n):
        print("The scaled co-ordinates of point " + str(i+1) + " are: (" +
              str(scale_x_points[i]) + "," + str(scale_y_points[i]) + ")")
        print()


def reflection(n, x_points, y_points):

    t = int(input("Enter the angle(in degrees) of inclination of the line through which the point will be reflected: "))
    y = int(input("Enter the y-intercept: "))
    rad_2t = math.radians(2*t)
    reflec_mat = np.zeros((3, 3), dtype=np.double)
    reflec_mat[0][0] = math.cos(rad_2t)
    reflec_mat[0][1] = math.sin(rad_2t)
    reflec_mat[0][2] = math.sin(rad_2t)*(-y)
    reflec_mat[1][0] = math.sin(rad_2t)
    reflec_mat[1][1] = -math.cos(rad_2t)
    reflec_mat[1][2] = (math.cos(rad_2t)+1)*y
    reflec_mat[2][0] = 0
    reflec_mat[2][1] = 0
    reflec_mat[2][2] = 1

    p = np.zeros((3, n), dtype=np.double)
    for i in range(0, n):
        p[0][i] = x_points[i]
        p[1][i] = y_points[i]
        p[2][i] = 1

    p1 = np.zeros((3, n), dtype=np.double)
    for i in range(0, 3):
        for j in range(0, n):
            p1[i][j] = 0
            for k in range(0, 3):
                p1[i][j] += reflec_mat[i][k] * p[k][j]

    reflec_x_points = [0]*n
    reflec_y_points = [0]*n

    for i in range(0, n):
        reflec_x_points[i] = round(p1[0][i])
        reflec_y_points[i] = round(p1[1][i])

    for i in range(0, n):
        print("The reflected co-ordinates of point " + str(i+1) + " are: (" +
              str(reflec_x_points[i]) + "," + str(reflec_y_points[i]) + ")")
        print()


def shearing(n, x_points, y_points):

    shx = float(input("Enter the shearing value for the x co-ordinate: "))
    shy = float(input("Enter the shearing value for the y co-ordinate: "))
    shear_x_points = [0]*n
    shear_y_points = [0]*n

    for i in range(0, n):
        shear_x_points[i] = round(x_points[i] + y_points[i]*shx)
        shear_y_points[i] = round(y_points[i] + x_points[i]*shy)

    for i in range(0, n):
        print("The sheared co-ordinates of point " + str(i+1) + " are: (" +
              str(shear_x_points[i]) + "," + str(shear_y_points[i]) + ")")
        print()


translation(n, x_points, y_points)
rotation(n, x_points, y_points)
scaling(n, x_points, y_points)
reflection(n, x_points, y_points)
shearing(n, x_points, y_points)
