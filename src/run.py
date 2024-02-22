import pygame

from canvas import Canvas
from runner import GameRunner

from game import GameState,GameLogic


#Get Canvas
pygame.init()
windowWidth = 480
windowHeight = 640

canvasCreator = lambda width, height: pygame.display.set_mode(width,height)
canvas = Canvas(canvasWidth,canvasHeight,canvasCreator)





