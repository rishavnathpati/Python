import sys
import pygame
import pygame_widget as pw


def setMousePosition(p):
    global x, ypos
    if p[0] < 500 and p[1] < 500:
        x = p[0]//inc
        y = p[1]//inc
