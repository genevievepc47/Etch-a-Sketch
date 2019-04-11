#pygame template
"""Genevieve Cohen
Period 10 Hnors computer programming (python)
etch a sketch
recreate the game
"""

import pygame
import sys
import random
import math


pygame.init()#initialize game engine
#logo = pygame.image.load("etch.gif")

#manage speed by introducing a clock
clock = pygame.time.Clock()

#set up the drawing surface
w = 660 
h = 500
size = (w,h) #tuple
surface = pygame.display.set_mode(size)

#set the window title bar
pygame.display.set_caption("Cohen Etch-A-Sketch")

# declare color constants
BLACK = (0  ,0  ,0  )
WHITE = (255,255,255)
RED =   (255,0  ,0  )
GREEN = (0  ,255,0  )
BLUE =  (0  ,0  ,255)
YELLOW =(255, 255, 0)
PINK =  (255,0  ,147)

'''
accepts the key pressed and the current color
1,2,3,4, black, red, green, blue
returns the new color depending on what key was pressed
'''
def getColorChoice(key, currentColor):
    if(key == pygame.K_1):
        color = BLACK
    elif(key == pygame.K_2):
        color = RED
    elif(key == pygame.K_3):
        color = GREEN
    elif(key == pygame.K_4):
        color = BLUE
    elif(key == pygame.K_5):
        color = YELLOW
    elif(key == pygame.K_6):
        color = PINK
    else:
        color = currentColor
    return color
    

'''
accepts: the current position of the brush and the keys
tests if any of the keys are being held down
moves the brush, tests if it is in the bounds
returns: the new position of the brush
'''
def moveBrush(brushPos, keys):
    if(keys[pygame.K_LEFT] == True): #if the left key is continually pressed
        brushPos[0] = brushPos[0] -w/19000 #move the brush left
        if(brushPos[0] < w/14 ): #if it is out of bounds on the left
            #move it right by the same amount 
            brushPos[0] = brushPos[0] + w/19000
    
    if(keys[pygame.K_RIGHT] == True): # if the right key is continually pressed
        brushPos[0] = brushPos[0] + w/19000 #move the brush right
        if(brushPos[0] >= w-w/12.5): #if it is out of bounds on the right
            #move the brush left by the same amount
            brushPos[0] = brushPos[0] - w/19000
    
    if(keys[pygame.K_UP] == True): # if the up key is continually pressed
        brushPos[1] = brushPos[1] - w/19000 #move the brush up 
        if( brushPos[1] <  h/12): #if it is out of bounds on the top
            brushPos[1] = brushPos[1] + w/19000 #move the brush down by the same amount
    
    if(keys[pygame.K_DOWN] == True): # if the down key is continually pressed
        brushPos[1] = brushPos[1] + w/19000 #move the brush down 
        if(brushPos[1] > h-h/5.59): #if it is out of bounds on the bottom
            brushPos[1] = brushPos[1] -w/19000
    
    return brushPos

'''
draws the brush at a certain position on the screen
input position as a tuple (maybe color later)

'''
def drawBrush(brushPos, brushColor):
    pygame.draw.ellipse(surface, brushColor, (brushPos[0], brushPos[1], w/100, w/100),0)

"""
draws the outer red box, the logo, and the white knob controls
"""
def drawScreen():
  
    
    pygame.draw.rect(surface, RED, (0,0,w, h/12),0) #draw top red box
    pygame.draw.rect(surface, RED,(0,0,w/14,h-h/6),0) #draw left red box
    pygame.draw.rect(surface, RED,(w-w/14,0,w/14,h-h/6),0) #draw right red box
    pygame.draw.rect(surface, RED, (0,h-h/6,w,h/6),0) #draw bottom red box (two times taller)
    
    pygame.draw.circle(surface, WHITE, (int(w/14), int(h-w/16)), int(w/20), 0) #draw left circle, 
    pygame.draw.circle(surface, WHITE, (int(w/14*13), int(h-w/16)), int(w/20), 0) #draw right circle, 
    
    #logo
    #logoSize =logo.get_rect().size #returns a tuple with the logo (width,height)
    #logoPos = [w/2-(logoSize[0]/2), h-h/13 - logoSize[1]/2]
    #surface.blit(logo, logoPos) #put the logo on the screen

def main():
    brushPos = [(w/2), h/2] #varibale to keep track of the position of the brush, tuple of [x,y] 
    fillWhite = False
   
    #initial game setup
    pygame.draw.rect(surface, WHITE, (0,0,w,h), 0)#draw the white background
    brushColor = BLACK
    drawScreen()
    #----------------------------------MAIN PROGRAM LOOP-----------------------------------------
    while(True):
        #the get continual pressed
        keys =  pygame.key.get_pressed()
        
        
        
        for event in pygame.event.get():
            if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #if they press escape
                pygame.quit()
                sys.exit()
            if(event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE): #if they press the sapce bar
                fillWhite = True   
            elif(event.type == pygame.KEYDOWN ):
                key = event.key
                brushColor = getColorChoice(key, brushColor)
        #game logic goes here
       
       
        
        #set background fill
        
        
        #drawing code goes here
        
       
        
        if (fillWhite== True): #if they have hit space bar, they want to reset the screen
            pygame.draw.rect(surface, WHITE, (0,0,w,h), 0)#draw the white background
            drawScreen() 
            brushPos = [(w/2), h/2] #reset brush position
            brushColor = BLACK
            fillWhite = False
    
        brushPos =  moveBrush(brushPos, keys)
        drawBrush(brushPos, brushColor)    
      
        pygame.display.update()
        
        
        
main() #call the main function