
import pygame
import random
import GUI

screen = pygame.display.set_mode( (512, 512), pygame.RESIZABLE )

run_program = True
dim0_size = 512
dim1_size = 512

class Canvas:
    def __init__(self, width = 512, height = 512) -> None:
        
        self.width = width
        self.height = height
        
        self.surface = pygame.Surface((width, height))
        self.surface.fill((255,255,255)) # test function
        
        self.x_offset = 0
        self.y_offset = 0
        
        # if this is true, then the canvas and thus the display needs to be redrawn
        self.undrawn = False
        
        self.scale = 1

    def draw(self, window_screen):
        
        surf_display = pygame.transform.scale(self.surface, (self.width*self.scale, self.height*self.scale))
        pygame.Surface.blit(window_screen, surf_display, (self.x_offset, self.y_offset))

    def tick(self):
        self.scale *= 0.95
        






myCanvas = Canvas()

mainGUI = GUI.GUI(screen)

r_range = random.randrange(255)
g_range = random.randrange(255)
b_range = random.randrange(255)

fill_color = (255, 255, 255)

# for dim0 in range(dim0_size):
#     for dim1 in range(dim1_size):
#         fill_color = (random.randrange(r_range), random.randrange(g_range), random.randrange(b_range))
#         pygame.draw.rect(screen, fill_color, pygame.Rect(dim0, dim1, 1, 1))

pygame.draw.rect(screen, fill_color,pygame.Rect(0,0,512,512))

pygame.display.flip()


class Pencil():
    def __init__(self) -> None:
        # this tool is currently selected
        self.active = True

        # should currently be drawing pixels onto canvas
        self.drawing = False

        # some previous coords so the mouse actually draws lines
        self.previous_pos = (0, 0)

    def mouse_down(self):  
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = True

    def mouse_up(self):  
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = False

    def tick(self, canvas_obj):
        if self.drawing:
            current_pos = pygame.mouse.get_pos()
            pygame.draw.line(canvas_obj.surface, (0, 0, 0), current_pos, self.previous_pos)
            self.previous_pos = current_pos
            pygame.display.flip()





pencil_tool = Pencil()
loaded_image = pygame.Surface((512, 512))
image_displayed = False

while run_program:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            run_program = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            pencil_tool.mouse_down()
        if event.type == pygame.MOUSEBUTTONUP:
            pencil_tool.mouse_up()

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_s:
                pygame.image.save(screen, "test_file.png")
            if event.key == pygame.K_o:
                loaded_image = pygame.image.load("test_file.png")
                image_displayed = True
            #Added for easy closing since I don't want to move my mouse
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run_program = False
                break

    if not run_program:
        break
    
    if image_displayed:
        screen.fill((255, 255, 255))
        screen.blit(loaded_image, (0, 0))
        pygame.display.update()

    pencil_tool.tick(myCanvas)

    myCanvas.draw(screen)
    #myCanvas.tick()

    mainGUI.draw()

    pass # other that happens every tick can go here
        
    pygame.display.flip()
