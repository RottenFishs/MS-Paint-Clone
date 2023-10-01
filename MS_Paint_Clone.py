#Starter Code from https://www.geeksforgeeks.org/how-to-create-ms-paint-clone-with-python-and-pygame/

import pygame


 
# Making canvas (The numbers manipulate the size)
screen = pygame.display.set_mode((1000, 700))
 
# Sets the title of the app
pygame.display.set_caption('MS Paint Clone')
 
# Variables to help with the event listener
draw_on = False
last_pos = (0, 0)
 
# Radius of the Brush (Sets size of brush)
radius = 2
 
 
# A function that makes drawing more smooth and not a bunch of circles
def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0]-start[0]
    Yaxis = end[1]-start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0]+float(i)/dist*Xaxis)
        y = int(start[1]+float(i)/dist*Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)
 
 
try:
    while True:
        e = pygame.event.wait()
         
        if e.type == pygame.QUIT:
            raise StopIteration
             
        if e.type == pygame.MOUSEBUTTONDOWN:         
            # Selecting random Color Code
            color = (0,100,0)
            # Draw a single circle wheneven mouse is clicked down.
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        # When mouse button released it will stop drawing   
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        # It will draw a continuous circle with the help of roundline function.   
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos,  radius)
            last_pos = e.pos
        pygame.display.flip()
 
except StopIteration:
    pass
   
# Quit
pygame.quit()