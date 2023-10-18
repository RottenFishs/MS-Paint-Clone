
import pygame
import random
import GUI

screen = pygame.display.set_mode( (512, 512), pygame.RESIZABLE )

run_program = True
dim0_size = 512
dim1_size = 512

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

    if not run_program:
        break
    
    pencil_tool.tick(myCanvas)

    myCanvas.draw(screen)
    #myCanvas.tick()

    mainGUI.draw()

    pass # other that happens every tick can go here

    pygame.display.flip()
