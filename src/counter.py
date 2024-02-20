import pygame

seven_segment_display = [[1,1,1,1,1,1,0],
                         [0,1,1,0,0,0,0],
                         [1,1,0,1,1,0,1],
                         [1,1,1,1,0,0,1],
                         [0,1,1,0,0,1,1],
                         [1,0,1,1,1,1,1],
                         [1,1,1,0,0,1,0],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,0,1,1]]


orientation = lambda k,d,o = (d,kd) if o else (kd,d)
orientation_bits = [0,1,1,0,1,1,0]
pts = [(d,0),((k+1)*d,d),((k+2)*d,(k+1)*d),(d,(2*k+1)*d),(0,(k+2)*d),(0,d)]



class Counter:
    def __init__(self,position,size):
        self.position = position
        self.size = size

    def draw_counter(self,value):


    def draw_counter(self,screen,colour):
        dh = lambda x,y,l: pygame.Rect(x,y,l,l*4)

        pygame.draw.rect(screen,colour,dr(x+size,y,size))
        pygame.draw.rect(screen,colour,pygame.Rect(0,0,50,50))
        pygame.draw.rect(screen,colour,pygame.Rect(0,0,50,50))
        pygame.draw.rect(screen,colour,pygame.Rect(0,0,50,50))
        pygame.draw.rect(screen,colour,pygame.Rect(0,0,50,50))
        pygame.draw.rect(screen,colour,pygame.Rect(0,0,50,50))
        pygame.draw.rect(screen,colour,pygame.Rect(0,0,50,50))



