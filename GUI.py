import pygame


def makeGUI(screen):

    pygame.draw.rect(screen,(187, 192, 199),pygame.Rect(0,0,512,50))
    class ToolButton():

        def __init__(self, x, y, inactive, active):
            self.active = False
            self.clicked = False
            self.activeImage = active
            self.inactiveImage = inactive

            self.image = inactive
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)

        
        def draw(self):
            position = pygame.mouse.get_pos()

            if self.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True

                    if self.active is False:
                        self.image = self.activeImage
            if pygame.mouse.get_pressed()[0] is 0:
                self.clicked = False
                    

            screen.blit(self.image, (self.rect.x, self.rect.y))


    

    # Brush tool
    brushInactiveImage = pygame.image.load("Images/brush_inactive.png")
    brushActiveImage = pygame.image.load("Images/brush_active.png")
    brush = ToolButton(20, 20, brushInactiveImage, brushActiveImage)
    brush.draw()

    eraserInactiveImage = pygame.image.load("Images/eraser_inactive.png")
    eraserActiveImage = pygame.image.load("Images/eraser_active.png")
    eraser = ToolButton(50, 20, eraserInactiveImage, eraserActiveImage)
    eraser.draw()

    # Fill tool
    fillInactiveImage = pygame.image.load("Images/fill_inactive.png")
    fillActiveImage = pygame.image.load("Images/fill_active.png")
    fill = ToolButton(80, 20, fillInactiveImage, fillActiveImage)
    fill.draw()

    # Panning tool
    panningInactiveImage = pygame.image.load("Images/panning_inactive.png")
    panningActiveImage = pygame.image.load("Images/panning_active.png")
    panning = ToolButton(110, 20, panningInactiveImage, panningActiveImage)
    panning.draw()

    # Pencil tool
    pencilInactiveImage = pygame.image.load("Images/pencil_inactive.png")
    pencilActiveImage = pygame.image.load("Images/pencil_active.png")
    pencil = ToolButton(140, 20, pencilInactiveImage, pencilActiveImage)
    pencil.draw()

    # Eyedropper tool
    eyedropperInactiveImage = pygame.image.load("Images/eyedropper_inactive.png")
    eyedropperActiveImage = pygame.image.load("Images/eyedropper_active.png")
    eyedropper = ToolButton(170, 20, eyedropperInactiveImage, eyedropperActiveImage)
    eyedropper.draw()
    pygame.display.flip()

