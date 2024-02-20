import pygame
import sys

from vector import Vector as vec
from entities import * 
from functools import partial
from counter import Counter as cc


##For a ping pong game only three 2D vector should be fine.

pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong Game In Python')

#Constants for now
PLAYER_DIM = vec(x=10,y=40)
PLAYER_VELOCITY = vec(x=0,y=0)
PLAYER_VELOCITY_Y_MAG = 5
BALL_SIZE = vec(x=10,y=10) 
BALL_VELOCITY = vec(x=-2,y=0) 


pos_ball_0 = vec(x=screen_width//2,y=screen_height//2)
pos_p1_0 = vec(x=10,y=screen_height//2)
pos_p2_0 = vec(x=screen_width-20,y=screen_height//2)

ball = Ball(pos_ball_0,BALL_VELOCITY,BALL_SIZE)
player_1 = Player(pos_p1_0,PLAYER_VELOCITY,PLAYER_DIM)
player_2 = Player(pos_p2_0,PLAYER_VELOCITY,PLAYER_DIM)



def boundary_check(obj):
    if obj.get_position().x <= 0 or obj.get_position().x >= screen_width:
        obj.set_position(vec(x=screen_width//2,y=screen_height//2))





#Game Loop
clk = pygame.time.Clock();       
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        kp = lambda a,b,c : -1 if a == b else (1 if a == c else 0)
        ud = kp(event.type,pygame.KEYDOWN,pygame.KEYUP)
        if(abs(ud)):
            delta_v = lambda ek,ku,kd,mag : ud*mag if ek == kd else (-1*ud*mag if ek == ku else 0)
            player_1.update_velocity(vec(x=0,y=delta_v(event.key,ord('s'),ord('w'),PLAYER_VELOCITY_Y_MAG)))
            player_2.update_velocity(vec(x=0,y=delta_v(event.key,pygame.K_DOWN,pygame.K_UP,PLAYER_VELOCITY_Y_MAG)))

    collide = lambda a,b : a >= b 
    bounce = lambda vx,vy : vec(x=-2*vx,y=-2*vy)


    #TODO: make this more intuitive
    def check_collision():
        if(collide(ball.get_position().y+ball.get_size().y+1,screen_height) or collide(0,ball.get_position().y-1)):
            ball.update_velocity(bounce(0,ball.get_velocity().y))
        if(collide(ball.get_position().x,screen_width+ball.get_size().x) or collide(-ball.get_size().x,ball.get_position().x)):
            ball.set_position(vec(x=screen_width//2,y=screen_height//2)) 
        if(collide(player_1.get_position().x+player_1.get_size().x+1,ball.get_position().x)) and (collide(ball.get_position().y+ball.get_size().y,player_1.get_position().y) and collide(player_1.get_position().y+player_1.get_size().y+1,ball.get_position().y)):
            ball.update_velocity(bounce(ball.get_velocity().x,0))
        if(collide(ball.get_position().x+ball.get_size().x+1,player_2.get_position().x)) and (collide(ball.get_position().y+ball.get_size().y,player_2.get_position().y) and collide(player_2.get_position().y+player_2.get_size().y+1,ball.get_position().y)):
            ball.update_velocity(bounce(ball.get_velocity().x,0))

    check_collision()

    

          
    ball.move()                 

    player_1.move()
    ##if not (collide(screen_height,player_2.get_position().y+player_2.get_size().y) or collide(0,player_2.get_position().y)):
    player_2.move()

    screen.fill(black)
    c1 = cc(5)
    print(type(screen))
    c1.draw_counter(screen)
 
    pygame.draw.rect(screen,white,pygame.Rect(ball.get_position().x,ball.get_position().y,ball.get_size().x,ball.get_size().y))
    pygame.draw.rect(screen,white,pygame.Rect(player_1.get_position().x,player_1.get_position().y,player_1.get_size().x,player_1.get_size().y))
    pygame.draw.rect(screen,white,pygame.Rect(player_2.get_position().x,player_2.get_position().y,player_2.get_size().x,player_2.get_size().y))

    #Handle Collision


    pygame.display.flip()

    clk.tick(60)

pygame.quit()





