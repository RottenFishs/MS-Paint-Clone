import pygame

class GUI():
    class ToolButton():
        def __init__(self, x, y, inactive, active,screen):
            self.state = False
            self.clicked = False
            self.activeImage = active
            self.inactiveImage = inactive
            self.screen = screen

            if not self.state:
                self.image = self.inactiveImage
            else:
                self.image = self.activeImage
            
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.topleft = (x,y)
        
        def draw(self):
            position = pygame.mouse.get_pos()

            if self.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.state = not self.state

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            if not self.state:
                self.image = self.inactiveImage
            else:
                self.image = self.activeImage
            
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
            pygame.display.flip

    def __init__(self,screen):
        self.screen = screen
        # Brush tool
        brushInactiveImage = pygame.image.load("Images/brush_inactive.png")
        brushActiveImage = pygame.image.load("Images/brush_active.png")
        brush = GUI.ToolButton(20, 20, brushInactiveImage, brushActiveImage,self.screen)
        brush.draw()

        eraserInactiveImage = pygame.image.load("Images/eraser_inactive.png")
        eraserActiveImage = pygame.image.load("Images/eraser_active.png")
        eraser = GUI.ToolButton(50, 20, eraserInactiveImage, eraserActiveImage,self.screen)
        eraser.draw()

        # Fill tool
        fillInactiveImage = pygame.image.load("Images/fill_inactive.png")
        fillActiveImage = pygame.image.load("Images/fill_active.png")
        fill = GUI.ToolButton(80, 20, fillInactiveImage, fillActiveImage,self.screen)
        fill.draw()

        # Panning tool
        panningInactiveImage = pygame.image.load("Images/panning_inactive.png")
        panningActiveImage = pygame.image.load("Images/panning_active.png")
        panning = GUI.ToolButton(110, 20, panningInactiveImage, panningActiveImage,self.screen)
        panning.draw()

        # Pencil tool
        pencilInactiveImage = pygame.image.load("Images/pencil_inactive.png")
        pencilActiveImage = pygame.image.load("Images/pencil_active.png")
        pencil = GUI.ToolButton(140, 20, pencilInactiveImage, pencilActiveImage,self.screen)
        pencil.draw()

        # Eyedropper tool
        eyedropperInactiveImage = pygame.image.load("Images/eyedropper_inactive.png")
        eyedropperActiveImage = pygame.image.load("Images/eyedropper_active.png")
        eyedropper = GUI.ToolButton(170, 20, eyedropperInactiveImage, eyedropperActiveImage,self.screen)
        eyedropper.draw()

        self.brush = brush
        self.eraser = eraser
        self.fill = fill
        self.panning = panning
        self.pencil = pencil
        self.eyedroppper = eyedropper
        pygame.display.flip

    def draw(self):
        pygame.draw.rect(self.screen,(187, 192, 199),pygame.Rect(0,0,512,50))
        self.brush.draw()
        self.eraser.draw()
        self.fill.draw()
        self.panning.draw()
        self.pencil.draw()
        self.eyedroppper.draw()
        pygame.display.flip



