import pygame

class GUI():
    class ToolButton():
        STATIC_SELECTED = "pencil"
        def __init__(self, x, y, inactive, active,screen,name):
            self.state = False
            self.clicked = False
            self.activeImage = active
            self.inactiveImage = inactive
            self.screen = screen
            self.mouse_was_pressed = False
            self.image = self.inactiveImage
            self.name = name
            
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.topleft = (x,y)
        

        def draw(self):
            position = pygame.mouse.get_pos()
            mouse_is_pressed = pygame.mouse.get_pressed()[0] == 1
            if self.rect.collidepoint(position):
                if  mouse_is_pressed and self.clicked == False and not self.mouse_was_pressed:
                    self.clicked = True
                    self.state = True
                    GUI.ToolButton.STATIC_SELECTED = self.name

            if GUI.ToolButton.STATIC_SELECTED != self.name:
                self.state = False

            if not mouse_is_pressed:
                self.clicked = False

            
            if not self.state:
                self.image = self.inactiveImage
            else:
                self.image = self.activeImage
            
            self.screen.blit(self.image, (self.rect.x, self.rect.y))
            pygame.display.flip
            self.mouse_was_pressed = mouse_is_pressed

        def setActive(self,isActive):
            if isActive:
                self.state = True
            else:
                self.state = False


    # class ColorButton():


    def __init__(self,screen):
        self.screen = screen


        # Pencil tool
        pencilInactiveImage = pygame.image.load("Images/pencil_inactive.png")
        pencilActiveImage = pygame.image.load("Images/pencil_active.png")
        pencil = GUI.ToolButton(20, 20, pencilInactiveImage, pencilActiveImage,self.screen, "pencil")
        pencil.draw()
        pencil.setActive(True)

        #Eraser tool
        eraserInactiveImage = pygame.image.load("Images/eraser_inactive.png")
        eraserActiveImage = pygame.image.load("Images/eraser_active.png")
        eraser = GUI.ToolButton(50, 20, eraserInactiveImage, eraserActiveImage,self.screen, "eraser")
        eraser.draw()

        # Fill tool
        fillInactiveImage = pygame.image.load("Images/fill_inactive.png")
        fillActiveImage = pygame.image.load("Images/fill_active.png")
        fill = GUI.ToolButton(80, 20, fillInactiveImage, fillActiveImage,self.screen, "fill")
        fill.draw()

        # Panning tool
        panningInactiveImage = pygame.image.load("Images/panning_inactive.png")
        panningActiveImage = pygame.image.load("Images/panning_active.png")
        panning = GUI.ToolButton(110, 20, panningInactiveImage, panningActiveImage,self.screen, "panning")
        panning.draw()

        # Brush tool
        brushInactiveImage = pygame.image.load("Images/brush_inactive.png")
        brushActiveImage = pygame.image.load("Images/brush_active.png")
        brush = GUI.ToolButton(140, 20, brushInactiveImage, brushActiveImage,self.screen, "brush")
        brush.draw()

        # Eyedropper tool
        eyedropperInactiveImage = pygame.image.load("Images/eyedropper_inactive.png")
        eyedropperActiveImage = pygame.image.load("Images/eyedropper_active.png")
        eyedropper = GUI.ToolButton(170, 20, eyedropperInactiveImage, eyedropperActiveImage,self.screen, "eyedropper")
        eyedropper.draw()

        self.eraser = eraser
        self.fill = fill
        self.panning = panning
        self.pencil = pencil
        self.brush = brush
        self.eyedroppper = eyedropper

        pygame.display.flip

    def draw(self):
        #Grey Bar on top
        pygame.draw.rect(self.screen,(187, 192, 199),pygame.Rect(0,0,512,50))
        pygame.draw.rect(self.screen,(0, 0, 255),pygame.Rect(0,0,512,8))
        self.brush.draw()
        self.eraser.draw()
        self.fill.draw()
        self.panning.draw()
        self.pencil.draw()
        self.eyedroppper.draw()


        # pygame.draw.rect(self.screen,(255, 0, 0),pygame.Rect(300,5,15,15))
        # pygame.draw.rect(self.screen,(187, 192, 199),pygame.Rect(200,30,20,20))


        pygame.display.flip

    def getSelectedTool(self):
        return self.ToolButton.STATIC_SELECTED()



